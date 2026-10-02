from flask import Flask, render_template, request, jsonify
from motiondetection import MotionDetector
from dotenv import load_dotenv

import base64
import cv2
import numpy as np
import os
import threading
import smtplib
import datetime

from email.message import EmailMessage


load_dotenv()


app = Flask(__name__)



detector = MotionDetector()


SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "")


def send_motion_email(image):
    """
    Sends an email when motion is detected.

    Email credentials are NOT stored in the source code.
    They are read from environment variables.
    """

    if not SENDER_EMAIL or not SENDER_PASSWORD or not RECEIVER_EMAIL:
        print("Email settings are not configured.")
        return

    try:
        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # =============================Convert OpenCV image to JPG
        success, encoded_image = cv2.imencode(".jpg", image)

        if not success:
            print("Could not encode image.")
            return

        image_data = encoded_image.tobytes()

        message = EmailMessage()

        message["Subject"] = f"🚨 Motion Detected - {timestamp}"
        message["From"] = SENDER_EMAIL
        message["To"] = RECEIVER_EMAIL

        message.set_content(
            f"""
Motion has been detected by your Alarm Security System.

Time:
{timestamp}

The captured image is attached to this email.
"""
        )

        message.add_attachment(
            image_data,
            maintype="image",
            subtype="jpeg",
            filename="motion_detection.jpg"
        )

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(
                SENDER_EMAIL,
                SENDER_PASSWORD
            )

            server.send_message(message)

        print("Motion alert email sent successfully.")

    except Exception as error:
        print("Email error:", error)




@app.route("/")
def index():
    return render_template("index.html")




@app.route("/detect", methods=["POST"])
def detect_motion():

    try:

        data = request.get_json()

        if not data or "image" not in data:
            return jsonify({
                "success": False,
                "error": "No image received."
            }), 400

        image_data = data["image"]

        # ===============================Remove base64 prefix
        if "," in image_data:
            image_data = image_data.split(",", 1)[1]

        # ==============================Decode base64
        image_bytes = base64.b64decode(image_data)

        # =============================Convert bytes to NumPy array
        np_array = np.frombuffer(
            image_bytes,
            np.uint8
        )

        # =======================Convert to OpenCV image
        frame = cv2.imdecode(
            np_array,
            cv2.IMREAD_COLOR
        )

        if frame is None:
            return jsonify({
                "success": False,
                "error": "Invalid image."
            }), 400

        # ======================Resize frame
        frame = cv2.resize(
            frame,
            (640, 480)
        )

        # ===================Process motion
        motion_detected, motion_score = detector.detect(frame)

        email_sent = False

        # ===============Send email only when a new motion event starts
        if motion_detected and detector.should_send_alert():

            # =======Send email in background
            email_thread = threading.Thread(
                target=send_motion_email,
                args=(frame.copy(),)
            )

            email_thread.daemon = True
            email_thread.start()

            email_sent = True

        return jsonify({
            "success": True,
            "motion": motion_detected,
            "score": round(motion_score, 2),
            "email_sent": email_sent
        })

    except Exception as error:

        print("Detection error:", error)

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500



@app.route("/health")
def health():

    return jsonify({
        "status": "online",
        "application": "Alarm Security System"
    })



@app.route("/reset", methods=["POST"])
def reset_detector():

    detector.reset()

    return jsonify({
        "success": True,
        "message": "Motion detector reset."
    })


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )