print("1. type '+' for Addition.")
print("2. type '-' for Subtration.")
print("3. type '*' for Multiplication.")
print("4. type '/' for Division.")
print("5. type '//' for Floor division.")
print("6. type '%' for Moduler.")
print("7. type '**' for Power.")
choice = input("Firstly Select Operation : ")

num_1 = int(input("Enter Number 1 :"))
num_2 = int(input("Enter Number 2 :"))

match choice:
    case "+" : print("Addition is : ",num_1+num_2)
    case "-" : print("Subtration is : ",num_1-num_2)
    case "*" : print("Multiplication is : ",num_1*num_2)
    case "/" : print("Division is : ",num_1/num_2)
    case "//": print("Floor Division is : ",num_1//num_2)
    case "%" : print("Moduler is : ",num_1%num_2)
    case "**": print("Power is : ",num_1**num_2)
    case _   : print("Not a Valid Operation!!")

