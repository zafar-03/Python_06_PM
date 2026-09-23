# mystr = "Math,Science,English,Math"
# print(set(mystr.split(",")))
# mylist = [
#     {
#         "id"     :   (101,),
#         "name"   :   "Raj",
#         "age"    :   21,
#         "grade"  :   "B+",
#         "dob"    :   ("11-01-2000",),
#         "subject":   {"Math","Science"}
#     },
#     {
#         "id"     :   (102,),
#         "name"   :   "Rajesh",
#         "age"    :   21,
#         "grade"  :   "B+",
#         "dob"    :   ("11-01-2000",),
#         "subject":   {"Math","Science"}
#     }
# ]
# rollno = int(input("Enter : "))

# templist = mylist
# print(mylist,templist,sep="\n",end="\n\n\n")
# for element in mylist:
#     if rollno == element.get("id")[0]:
#         templist.remove(element)


# # remove 
# print(mylist,templist,sep="\n",end="\n\n\n")

# students = []
# print("Welcome")

# while True:
#     print("\nSelect :")
#     print("1. ")
#     print("2. ")
#     print("3. ")
#     print("4. ")
#     print("5. ")
#     print("6. ")

#     choice = int(input("Enter Your Choice : "))


#     if choice ==1:
#          print("\nEnter Details :")
#          students.append({
#                "id"     :   tuple(input("student ID :")),
#                "name"   :   input("Name :"),
#                "age"    :   input("Age :"),
#                "grade"  :   input("Grade :"),
#                "dob"    :   tuple(input("Date of Birth (YYYY-MM-DD) :")),
#                "subject":   set(input("Subjects (comma Seprated) :").split(","))
#          })   
#          print("\n____")

#     elif choice ==2:
#         #  loop 
#         pass
#     elif choice ==3:
#         #  User input 
#         # loop control statement 
#         pass 
#     elif choice ==4:
#         #  User input  : id 
#         #  for loop :
#             # condition : del element
#         pass
#     elif choice ==5:
#          print()
#     elif choice ==6:
#          break
#     else:
#          print()


#==================================
# keys = ["id","name","email"]
# values = [101,"Alice","alice@gmail.com"]

# mydict = {}

# for i in range(0,3):
#     mydict.setdefault(keys[i],values[i])


# print(mydict)


keys = ["id","name","email"]
values = [101,"Alice","alice@gmail.com"]

mydict = {}


for element in tuple(zip(keys,values)):
    mydict.setdefault(element[0],element[1])
    # mydict.__setitem__(element[0],element[1])

print(mydict)
