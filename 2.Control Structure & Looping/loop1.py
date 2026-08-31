# looping : 
# 1. for loop.
"""
for variablename in range(startingpoint,endingpoint):
    code
"""
# WAP to print 5 times "Hello".
# for i in range(1,6):
#     print(i)

# addition = 0
# print("The first 10 natural number is :")
# for i in range(1,11):
#     print(i ,end=" ")
#     addition+=i 

# print()
# print("The Sum is :",addition)


# n = int(input("Test Data :"))
# addition = 0
# print("The first",n,"natural number is :")
# for i in range(1,n+1):
#     print(i ,end=" ")
#     addition+=i 

# print()
# print("The Sum of Natural Number upto",n,"terms :",addition)
# print(f"The Sum of Natural Number upto {n} terms :",addition)

# addition = 0
# print("Test Data :")
# print("Input the 10 numbers :")
# for i in range(1,11):
#     addition+=int(input(f"Number-{i} :"))

# print("Expected Output :")
# print("The sum of 10 no is :",addition)
# print("The Average is :",addition/10)

# n1 = int(input("Enter Starting Value : "))
# n2 = int(input("Enter Stoping Value : "))

# for i in range(n1,n2+1):
#     print(i)

# "String Formating 1 : method    "
# f"    {variablename}       {}"
# Wap to print table of n.
# n = int(input("Enter table Value : "))
# for i in range(1,11):
#     print(f"{n} * {i} = {i*n}")



# 2. while loop.
"""
for i in range(1,12):
    code

intialization  
while (condition):
    code
    step (changed value)

"""
# i=1
# while i<=10:
#     print(i)
#     i+=1  # i = i+1
# 

# Infinite Loop
# while True:
#     user_data = int(input("Enter Data :"))
#     if user_data==0:
#         break



for i in range(10,101,10):
    print(i)