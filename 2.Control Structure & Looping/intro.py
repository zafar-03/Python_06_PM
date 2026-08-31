# 2. Control Statement  :
#  Eq, output print,logic

# a. Condition Control Statement 
    # if statement 
    # if-else statement 
    # elif (ladder if-else) statement 
    # nested if-else statement 
# ========================================
"""
1. If Statement: If-Block 
    Syntax : 
    if condition :
        //code

if code excute when your Condition is True.
"""
# WAP to Print "Welcome Sir" if User named is "Admin".

# user_name = input("Enter Your Name : ")

# if user_name == "Admin" :
#     print("Welcome Sir")



# ========================================
"""
1. If-else Statement: If-else Block 
    Syntax : 
    if condition :
        //code
    else:
        //code

if code excute when your Condition is True.
otherwise else code excuted.

"""
# user_name = input("Enter Your Name : ")

# if user_name == "Admin" :
#     print("Welcome Sir")
# else:
#     print("Authantication Failed!!")

# WAP to Check User Password Valid or not.

# password = int(input("Enter Your Password  : "))

# if (password == 1234):
#     print("Login Succesfully")
# else:
#     print("Incorrect Password")


# WAP to check  User is Admin or Not.
# username = Admin  password = admin@123

user_name = input("Enter Username : ")
password = input("Enter Your Password : ")


if user_name == "Admin" and password =="admin@123" :
    print("Login Successful")
else:
    print("Something Wrong")

# ========================================
"""
1. Write a C program to accept two integers and check whether they are equal. (6)(3)


2.Write a C program to check whether a given number is positive or negative.(4)


3.Write a C program to check whether a given number is even and divisable by 3.(5)

4.Write a C program to read the age of a candidate and determine whether he is eligible to cast his/her own vote.
(1)

5.Write a C program to read the value of an integer m and display the value of n is 1 when m is larger than or Equal to 0,-1 when m is less than 0.
Test Data : -5
Expected Output :
The value of n = -1
(2)

"""


# b. Loop Control Statement 