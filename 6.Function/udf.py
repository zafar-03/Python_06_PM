# Syntax : 


# USER DEFINE  FUNCTION
# There are Four ways : 

# 1. TNRN : take nothing return nothing     : without argument and without return type
"""
step 1: create function : 

def functioname():
    code

    
step 2 : call/invoked/use
functionname()
"""
# def greeting():
#     print("Welcome Back!!")
#     print("How are you ? ")

# greeting()

# 2. TSRN : take something return nothing   : with argument and without return type 
"""
step : 1 create function 

def functioname(variablename):
    code 

step : 2 
functionname(value)

"""
# def greeting(username):      # parameter
#     print("Welcome Back",username)

# greeting("Raj")        # values  : argument 




# def addition(value1,value2):
#     print("Addition is :",value1+value2)

# addition(11,12)

# addition(34,5)





# 3. TNRS : take nothing return something   : without argument and with return type 
"""
Syntax : 
step : 1 creation 
def functionname():
    code  (optional)
    return ___

functionname()



any : return  : 
1. return data : use 
2. return data : store(variable)
"""
# def pi():
#     return 3.14

# print(12*pi())

# value_of_pi = pi()

# print(value_of_pi*11)
# print(value_of_pi*21)




# 4. TSRS : take something return something : with argument and with return type 
"""
step : 1 create function 

def functioname(variablename):
    return __ 

step : 2 
functionname(value)

"""

# def result(marks):
#     if marks > 35 :
#         return "Pass"
#     else:
#         return "Fail"

# print(result(12))
# print(result(52))


#===========================================
# Arbitrary arguments (*args) :

# def addition(n1,n2):
#     print(n1,n2)

# addition(1,2,5)

# def addition(*args):
#     sum_of_element = 0
#     for element in args:
#         sum_of_element+=element
#     print("Addition is :",sum_of_element)


# addition(11)
# addition(11,12)

# addition(11,12,40,50,60,20)




#===========================================
#  Keyword arguments (**kwargs) : 


# def userdata(name):
#     print(name)

# userdata(name="Raj")
# userdata(name="Raj",lname="shah")

# def userdata(**kwargs):
#     print(kwargs)

# userdata(name="Raj")
# userdata(name="Raj",lname="shah")



# def addition(**kwargs):
#     print(kwargs)

# addition(values1=11,value2=12)



def calculator():
    """ 
    Print Data 1 to 1
    Print Data End
    """
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")


# calculator()

print(calculator.__doc__)

# donder