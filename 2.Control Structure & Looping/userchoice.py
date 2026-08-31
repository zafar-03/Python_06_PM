# print("1. Intger")
# print("2. String")
# print("3. Boolean")

# choice = int(input("Enter your Choice : "))
# if choice==1:
#     print("Intger Operation")
# elif choice==2:
#     print("String Operation")
# elif choice==3:
#     print("Boolean Operation")
# else:
#     print("Not Valid")
# ======================================
# match case : 


print("1. Intger")
print("2. String")
print("3. Boolean")

choice = int(input("Enter your Choice : "))
match choice:
    case 1 : print("Intger Operation")
    case 2 : print("String Operation")
    case 3 : print("Boolean Operation")
    case _ : print("not Available")