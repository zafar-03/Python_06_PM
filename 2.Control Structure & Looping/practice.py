# while True:
# 	num = int(input("Enter Number : ")) 
# 	if num==0:
# 		break


# while not(int(input("Enter Number : ")) == 0) :
# 	print("Move Forward")


# for i in range(1,11):
#     print(i*i)

# print(i*i for i in range(1,11))

# i=10
# while i>=1 and i<=50:
#     if i % 2 == 0:
#         print(i)
#     i+=1


# for i in range(10,0,-1):
#     print(i)


# for i in range(0,10,-1):
#     print(i)
#=================================
# import random 


# random_number = int(random.random()*101)
# total_life = 10

# while True:
#     num = int(input("Guess the Number(1-100) : "))
#     if num<1 or num>100:
#         print("You are cross the Limit")
#         break

#     total_life-=1
#     if num == random_number:
#         print("You Win!!")
#         break
#     elif total_life == 0:
#         print("Game over. You Lost Game.")
#         break
#     elif num > random_number:
#         print("Try to Guess Lower Value !!")
#     elif num < random_number:
#         print("Try to Guess Higher Value !!")


#==================================
# import random
# my_list = ["Rock","Paper","Scissor"]
# print("Rock")
# print("Paper")
# print("Scissor")

# while True:
#     computer_choice = my_list[int(random.random()*3)]
#     user_choice  = input("Enter your choice")
#     if (user_choice == "Rock" and computer_choice=="Scissor") or (user_choice == "Scissor" and computer_choice=="Paper") or (user_choice == "Paper" and computer_choice=="Rock") : 
#         print("You Win")
#     elif (computer_choice == "Rock" and user_choice=="Scissor") or (computer_choice == "Scissor" and user_choice=="Paper") or (computer_choice == "Paper" and user_choice=="Rock") : 
#             print("You Lost")
#     else:
#         print("Match Tie")

"""
rock  : rock     tie
      : paper    lost
      : sci      win

paper  : rock   win
        : paper tie
        : sci   lost

sci  : rock   lost
     : paper  win 
     : sci    tie
"""