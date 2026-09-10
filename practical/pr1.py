print("Welcome")


while True:
    print("\nSelect an Options:")
    print("1. Ptn")
    print("2. Number")
    print("3. Exit")
    choice = int(input("Enter your choice :"))

    match choice:
        case 1 : 
            print("1. for triangle")
            print("2. for square")
            choice = int(input("Enter your choice :"))
            num = int(input("Enter the No. of Row : "))
            match choice:
                case 1: 
                    for i in range(0,num):
                        for j in range(0,i+1):
                            print("*",end=" ")
                        print()


                case 2: 
                    for i in range(0,num):
                        for j in range(0,num):
                            print("*",end=" ")
                        print()


        case 2 : 
            start = 10
            end = 15
            for i in range(start,end+1):
                print(f"Number {i} is","Even" if i % 2 == 0 else "Odd")

        case 3 : break

print("Goodbye !")

#########################
# start = 10
# end = 15
# for i in range(start,end+1):
#     if i % 2 == 0:
#         print(f"Number {i} is Even")
#     else:
#         print(f"Number {i} is Odd")
n = 10
# print(f"Number {n} is","Even" if n % 2 == 0 else "Odd")