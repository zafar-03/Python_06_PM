# WAP to Check Given Number is +ve or +ve.

num_1 = int(input("Enter the Value of num_1 : "))

# if(num_1 >0):
#     print("+ve")
# else:
#     print("-ve")

# if(num_1 >0):
#     print("+ve")
# elif(num_1 == 0):
#     print("Number is Zero")
# else:
#     print("-ve")

# WAP to Check Given Number is +ve (and divisable by 3 or not) or -ve.



if(num_1 >0):
    if(num_1 % 3 == 0):
        print("+ve and / 3.")
    else:
        print("+ve but not  / 3.")
elif(num_1 == 0):
    print("Number is Zero")
else:
    print("-ve")