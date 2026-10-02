# user_input= input("Enter your name : ")
# print(user_input,"And its length is",len(user_input))

                                                 #  Conditional statements 
# marks=int(input('enter your marks :'))
# if( marks>=90):
#     print("Grade A")
# elif(marks>=80 and marks<90):
#     print('Grade B')
# elif(marks>=70 and marks<80):
#     print("Grade C")
# else:
#     print('Grade D')
                               
                                                  #   list and tuples
# list=[]
# list.insert(0,5)
# list.insert(1,10)
# list.insert(0,6)
# print(list)
# list.remove(6)
# list.append(9)
# list.append(1)
# list.sort()
# print(list)
# list.pop(3)
# list.reverse()
# print(list)

# l1=[10,80,90,50,20,40,30]
# print(l1.pop())
# print(l1.pop())
# print(l1.pop())
# print(l1.reverse())
# print(l1.sort())
# print(l1)
# print(l1.append(12))
# print(l1[0:3])
# print(l1[4])
# print(l1.insert(1,8))
# print(l1.insert(1,8))
# print(l1.remove(8))
# print(l1[::-1])
# print(l1)
# print(type(l1))

# l2=[1,1,0]
# # x=l2.copy()
# # x.reverse()
# s=l2[::-1]
# print(s)
# if(s==l2):
#     print("palindrome")
# else:
#     print("not palindrome")


# tup=(1,2,3,4,5,6)
# print(tup)
# print(len(tup))
# print(type(tup))
# print(tup[1:5])
                                                       #   Take user input and store it in the LIST Programme 
# user1=input("Enter your 1 favourite movies name: ")
# user2=input("Enter your 2 favourite movies name: ")
# user3=input("Enter your 3 favourite movies name: ")
# list1=[user1,user2,user3]
# print(list1)


                                                    #  Palidorne number Programe
# list1=[1,2,3,2,1]
# x=list1.copy()
# x.reverse()
# if(x==list1):
#     print(x,"this is a palidrone number")
# else:
#     print("This is not the palidrone number")    

                                                     # Dictionary and Nested Dictionary  
# info = {
#     'name':'sahil',
#     'age':27,
#     'is_adult':True,
#     'marks':[10,20,30,90],
#                 #   nested  dictionary
#     'subjects':{             
#         'chemistry':30,
#         'physics':80,
#         'mathematics':100
#     }
# }
# info['name']='SAHIL'
# info["salary"]=1500
# print(info['name1'])
# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get('name1'))
# print(info.update({'city':'Delhi'}))
# print(info['city'])

# info1={
#     'table':('apiece of furniture','list of facts & figures'),
#     'cat':'A samll animal'
# }
# print(info1)

                                                         # set 
# set1={45,67,'python','java','c++','c++'}
# set1.add(10)
# print(set1)

                                                         # Loops
# x=1
# while x<=100:                                    
#     print(x)
#     x +=1  

# x=100
# while x>=1:  
#     print(x)
#     x -=1   

# n=5
# i=1
# while i<=10:
#     y=n*i
#     print(y)
#     i +=1                                                   

# x=[1,2,3,4]
# index=0
# while len(x)>index :
#     print(x[index])
#     index+=1

# x=(1,5,6,3,4,2,8,9)
# n=int(input("enter the  number:"))
# index=0
# while len(x)>index :
#     if(x[index]==n):
#         print(f"{x[index]} is present at index {index}")
#     index+=1

# x=[56,455,74,52,55,22,54]
# for y in x:
#     print(y)
    
# z=(11,22,33,44,55,66,77,88,99)
# for  i in z:
#     print(i)


# x=[56,455,74,52,55,22,54]
# y=54
# index=0
# for i in x:
#     if(i==y):
#         print(f"{y} is present at index {index}") 
#     index +=1    
 
                                                     # function and recusion 
   
# s=[1,5,6,3,2,4] 
# z=[1,5,6,3,2,4,5,8,10000]                                                  
# def sk(x): 
#     y=len(x)                             /* Count length of list*/
#     return y
# print(sk(z))     

# list1=['kabir','arun','python']
# def print_list(x):
#     for i in x:                           /* print element of list*/
#         print(i, end="  ")  
# print_list(list1)        



# def factorial(x):
#     fact =1
#     for i in range(1,x+1):               
#         fact*=i
#     print(fact)
# factorial(6)


# def odd_even(x):   
#     if(x%2==0):
#         print("even")                    /* odd even programme*/
#     else:
#         print("odd")
# odd_even(7)           
                                      #    /* Recursion */
# def recursion(x):
#     if(x==0):
#         return
#     print(x)                           
#     recursion(x-1)
# recursion(5)  

# def numbers(x):
#     if(x==0):
#         return 0
#     return numbers(x-1)+x            /* sum of natural numbers */
# sum=numbers(5)
# print(sum)   

                                    # /* File I/O */

# f=open('sahil.txt')
# data=f.read()
# print(data)
# f.close()/

# f=open('sahil.txt','w')                             /* Write function */ 
# f.write("HELLO I AM SAHIL KADAM AND I AM A SOFTWARE DEVELOPER AND ALSO KNOW ABOUT THE PYTHON LANGUAGE AS WELL. ")

# f=open('sahil.txt','a')                          /* append function */
# f.write('phone number is 98999000000')

                                                  # With syntax
# with open("sahil.txt","w")as f:
#     f.write("sahil kadam")  

# import os 
# os.remove('sahil.txt')                          /* deleting the file */
# os.remove('sahils.txt')


# with open('practice.txt','a+') as f:
#     f.write("Hi everyone\nwe are learning file i/o\nusing python\nI like programming in python")

# with open('practice.txt','r') as f:
#    data=f.read()
# x=data.replace("python","java")
# print(x)


# with open('practice.txt','w') as f:
#    f.write(x)

# def check_word():
#     word="numbers"
#     with open('sahils.txt','r') as f:
#         data=f.read()
#         if( data.find(word) !=-1):
#             print("found")
#         else:
#             print("not found")
# check_word()  

# def check_word():
#     word="numbers"
#     data=True
#     line=1
#     with open('sahils.txt','r') as f:
#         data=f.readline()
#         if( word in data):
#             print(line)
#             return
#             line+=1
#     return -1     
# print(check_word())               


# count=1
# with open("sahils.txt",'r') as f:
#     data=f.read()
#     num=data.split(',')
#     for val in num:
#         if(int(val)%2==0):
#             count+=1
# print(count)            
        
                                                     # OOPS
# class sahil():
#     name= 'kadam'
#     rollno='23'
# s1=sahil()
# print(s1.name,s1.rollno)          

# class sahil:
#     def __init__(self,Name,rollno):
#         self.name=Name
#         self.rollno=rollno
#         print("processing is in  progress...") 
    
#     def  display(self):
#         print("Name : ",self.name,"\nRoll No.:",self.rollno)

# s1=sahil('sahilkadam',23)
# s1.display()
# print(s1.display) 

# class school:
#     def __init__(self,name,chem,phy,english):
#         self.name=name
#         self.chem=chem
#         self.phy=phy
#         self.english=english
    
#     def  display(self):
#          print("Name : ",self.name,"\nchem.:",self.chem,"\nphy.:",self.phy,"\nenglish.:",self.english)

#     def avg(self):
#         average=(self.chem + self.phy + self.english)/3
#         return average

# s1=school('sahil',30,50,80)
# s1.display()
# print(f"average marks are {s1.avg()}")

# class Account:
#     def __init__(self,account_no, balance):
#         self.account_no=account_no
#         self.balance=balance

#     # Static method 
#     @staticmethod
#     def hello():
#         print("hello world")
        
#     # debit method
#     def  withdrawal(self,amount):
#         self.balance -=amount
#         print("The balance is",amount)

#     #  credit metod
#     def deposite(self,amount):
#         self.balance += amount
#         print("Your new  Balance is",amount)
         

# a=Account(12121,1000)
# a.withdrawal(100)
# a.deposite(200)
# a.hello()
# print(f"Account number is: {a.account_no} \nand Balance is Rs:{a.balance}")

# class student:
#     def __init__(self,name):
#         self.name=name
# s=student("sahilkadam")
# print(s.name)
# # del s.name                                // it will delete the attribute name from object s
# # del s                                     // it will delete whole object s
# print(s.name)

                                                        # Private attribute and methods
# class Account:
#     def __init__(self, name,account_no,account_password):
#         self.name=name
#         self.account_no=account_no
#         self.__account_password = account_password      # private attribute
    
#     def hello(self):
#         print(f"Hello Your Account password is :{self.__account_password}")

# a=Account("SAHIL KADAM",122553,558899)
# a.hello()                                                      # accessing the private attributes
# print(f"Account holder name: {a.name} \n account number is: {a.account_no}")   


# class student:
#     name='sahilkadam'
    
    # @classmethod                                   # class method
#     def  change_name(cls,name):
#         cls.name=name
        # return name

# s=student()
# print(s.name)
# s.change_name('python')
# print(s.name)
# print(student.name)

# class student:

#     def __init__(self,sub1,sub2,sub3):
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3
    
#     @property                                              #  property decorator
#     def percentage(self):
#         return str((self.sub1  + self.sub2 + self.sub3)/3 )
      

# s=student(67,74,85)
# s.sub2=46                                                   # change the value accordnig to need
# print(s.sub2)
# print(s.percentage)

# s={1,2,3,4,5}
# v={8,7,1,2,3}
# x=s | v
# print(x)


# def factorial(x=6):
#     fact=1
#     for i in range(1,x+1):
#         fact *=i
#     print(fact)
#     # return fact
# s=factorial()
# print(s)

# l1=[1,2,3]
# y=1
# for i in range (0,len(l1)):
#     print(i)
#     y =y*l1[i] 
#     # print(1[i])  
# print(y)    

# l1=[1,2,3]
# y=0
# for i in range (0,len(l1)):
#     print(i)
#     y =y+l1[i] 
#     # print(1[i])  
# print(y)  

# class student:
#     def __init__(self,name):
#         self.names=name
#         # name="sk"
#         # lname="last"

#     def welcome(self):
#         print("welcome",self.names) 
# s=student("sahil")
# s.welcome()
# print(s.names)

# class student():
#     def __init__(self,sub1,sub2,sub3):
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3

#     def average(self):
#            print((self.sub1+self.sub2+self.sub3)/3) 

# s=student(99,97,98)
# s.average()  


# def divide(x,y):
#     try:
#         return x/y
#     except:
#         print("error is occured")
# s=divide(100,0)
# print(s)

# def fabinoicseries(n):
#     if(n<=0):
#         print("invalid input")
#     elif(n==0):
#         return 0
#     elif n==1 or n==2: 
#         return 1
#     else:
#         return fabinoicseries(n-1)+fabinoicseries(n-2)

# print(fabinoicseries(10))
            
            # password generator

# import random

# lowerCase="abcdefghijklmnopqrstuvwxyz"
# upperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# specialChar="!@#$%^&*()"
# numbers="1234567890"
# allChar=lowerCase+upperCase+specialChar+numbers
# user_input=int(input("Enter the length"))
# password="".join(random.sample(allChar,user_input))
# print(password)

l1=int(11)
dig=l1
res=0

while(l1>0):
    rem=l1%10
    res=res*10+rem
    l1 = l1//10
if(dig==res):
    print("palindrome")
else:
    print("not palindrome")