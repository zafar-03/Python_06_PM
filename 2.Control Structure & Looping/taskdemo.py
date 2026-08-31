print("Press 1 for Pizza")
print("Press 2 for Burger")
print("Press 3 for Vadapav")

choice = int(input("Place Your Order : "))
match choice :
    case 1 : 
        print("You select Pizza!!")
        print("Press 1 for Corn-pizza")
        print("Press 2 for classic Pizza")
        choice = int(input("Select Pizza : "))
        match choice:
            case 1 : print("You've Selected Corn-Pizza")
            case 2 : print("You've Selected Classic-Pizza")
            case _ : print("Sorry Sir Not Available")

    case 2 : print("You select Burger!!")

    case 3 : print("You select Vadapav!!")

    case _ : print("Sorry Sir Not Available")
