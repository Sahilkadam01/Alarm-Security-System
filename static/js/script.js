const camera = document.getElementById("camera");

const canvas = document.getElementById("canvas");

const context = canvas.getContext("2d");

const startButton = document.getElementById("startButton");

const stopButton = document.getElementById("stopButton");

const resetButton = document.getElementById("resetButton");

const cameraPlaceholder =
    document.getElementById("cameraPlaceholder");

const systemStatus =
    document.getElementById("systemStatus");

const statusText =
    document.getElementById("statusText");

const detectionStatus =
    document.getElementById("detectionStatus");

const motionScore =
    document.getElementById("motionScore");

const motionBadge =
    document.getElementById("motionBadge");

const motionOverlay =
    document.getElementById("motionOverlay");

const alarmCard =
    document.getElementById("alarmCard");

const alarmStatus =
    document.getElementById("alarmStatus");


let stream = null;

let monitoring = false;

let processing = false;

let alarmActive = false;

let audioContext = null;

let oscillator = null;

let gainNode = null;


/* 
   START CAMERA
 */

async function startCamera() {

    try {

        stream = await navigator.mediaDevices.getUserMedia({

            video: {
                width: {
                    ideal: 1280
                },

                height: {
                    ideal: 720
                }
            },

            audio: false

        });


        camera.srcObject = stream;

        camera.style.display = "block";

        cameraPlaceholder.style.display = "none";


        monitoring = true;


        startButton.disabled = true;

        stopButton.disabled = false;


        systemStatus.classList.remove("offline");

        systemStatus.classList.add("online");

        statusText.textContent =
            "SYSTEM ONLINE";


        detectionStatus.textContent =
            "Active";


        /*
         * Browser audio normally requires a user interaction.
         * Start it after the user clicks Start Camera.
         */

        initializeAudio();


        monitorCamera();


    } catch (error) {

        console.error(
            "Camera error:",
            error
        );


        alert(
            "Camera access was denied or is unavailable. Please allow camera permission and try again."
        );

    }

}


/* STOP CAMERA */

function stopCamera() {

    monitoring = false;


    if (stream) {

        stream
            .getTracks()
            .forEach(
                track => track.stop()
            );

        stream = null;

    }


    camera.srcObject = null;

    camera.style.display = "none";

    cameraPlaceholder.style.display =
        "flex";


    startButton.disabled = false;

    stopButton.disabled = true;


    systemStatus.classList.remove("online");

    systemStatus.classList.add("offline");

    statusText.textContent =
        "SYSTEM OFFLINE";


    detectionStatus.textContent =
        "Inactive";


    stopAlarm();

}


/* ************************************************* AUDIO ************************************************************* */

function initializeAudio() {

    try {

        audioContext =
            new (
                window.AudioContext ||
                window.webkitAudioContext
            )();

    } catch (error) {

        console.error(
            "Audio initialization error:",
            error
        );

    }

}


/* **************************************************START ALARM ************************************************** */

function startAlarm() {

    if (alarmActive) {
        return;
    }


    alarmActive = true;


    alarmCard.classList.add("active");

    alarmStatus.textContent =
        "MOTION DETECTED";


    motionOverlay.classList.add("active");


    motionBadge.classList.add(
        "detected"
    );

    motionBadge.innerHTML =
        "<span></span> Motion Detected";


    /*
     * Generate browser alarm sound.
     */

    if (audioContext) {

        try {

            oscillator =
                audioContext.createOscillator();

            gainNode =
                audioContext.createGain();


            oscillator.type =
                "sawtooth";


            oscillator.frequency.value =
                850;


            gainNode.gain.value =
                0.08;


            oscillator.connect(
                gainNode
            );

            gainNode.connect(
                audioContext.destination
            );


            oscillator.start();


        } catch (error) {

            console.error(
                "Alarm audio error:",
                error
            );

        }

    }


    /*
     * Stop alarm automatically
     * after a short period.
     */

    setTimeout(() => {

        stopAlarm();

    }, 4000);

}


/* *********************************************STOP ALARM ******************************************************/

function stopAlarm() {

    alarmActive = false;


    if (oscillator) {

        try {

            oscillator.stop();

        } catch (error) {

            // Already stopped
        }

        oscillator.disconnect();

        oscillator = null;

    }


    if (gainNode) {

        gainNode.disconnect();

        gainNode = null;

    }


    alarmCard.classList.remove(
        "active"
    );


    alarmStatus.textContent =
        "Normal";


    motionOverlay.classList.remove(
        "active"
    );


    motionBadge.classList.remove(
        "detected"
    );


    motionBadge.innerHTML =
        "<span></span> Monitoring";

}


/* *******************************************************MONITOR CAMERr**************************************************** */

async function monitorCamera() {

    if (!monitoring) {
        return;
    }


    if (
        camera.readyState >=
        HTMLMediaElement.HAVE_CURRENT_DATA
    ) {

        await processFrame();

    }


    /*
     * Process roughly every 300ms.
     */

    setTimeout(
        monitorCamera,
        300
    );

}


/* ******************************************PROCESS FRAME *********************************************** */

async function processFrame() {

    if (processing) {
        return;
    }


    processing = true;


    try {

        context.drawImage(
            camera,
            0,
            0,
            canvas.width,
            canvas.height
        );


        const imageData =
            canvas.toDataURL(
                "image/jpeg",
                0.65
            );


        const response =
            await fetch(
                "/detect",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        image: imageData
                    })

                }
            );


        const result =
            await response.json();


        if (
            result.success
        ) {

            motionScore.textContent =
                result.score;


            if (result.motion) {

                startAlarm();

            }

        } else {

            console.error(
                result.error
            );

        }

    } catch (error) {

        console.error(
            "Frame processing error:",
            error
        );

    }


    processing = false;

}


/* ****************************************************** RESET ************************************************** */

async function resetDetection() {

    stopAlarm();


    try {

        await fetch(
            "/reset",
            {
                method: "POST"
            }
        );

        motionScore.textContent =
            "0";

    } catch (error) {

        console.error(
            "Reset error:",
            error
        );

    }

}


/* **************************************************EVENTS*********************************** */

startButton.addEventListener(
    "click",
    startCamera
);


stopButton.addEventListener(
    "click",
    stopCamera
);


resetButton.addEventListener(
    "click",
    resetDetection
);


/* *************************************** PAGE CLOSE******************************************************** */

window.addEventListener(
    "beforeunload",
    stopCamera
);