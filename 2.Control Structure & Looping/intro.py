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



# b. Loop Control Statement 

