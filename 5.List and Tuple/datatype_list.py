# List : 
# It's Collection of Data which is same or Different Datatype.
# Changable  : add ,delete, update
# Ordered 
# Index : Available

"""
Syntax : 
1. Empty List : 
variable_name = []

2. List with data : 
variable_name = [11,23,45]
variable_name = ["Raj","sahil"]
variable_name = [11,23,"Raj",True,3.14]

"""

# my_list = []
# print(my_list)
# print(type(my_list))



# my_list = [11,12,34,-45]
# my_list = ["Raj","shah"]
# my_list = [11,12,34,"Raj",True,12j+2]


# print(my_list)
# print(type(my_list))



# my_list =  [11,23,45,74,23,56,2,4]

# print(my_list)

# for element in my_list:
#     print(element)

# print(len(my_list))

# for index in range(0,len(my_list)):
#     print(my_list[index])


# Indexing : 
# my_list =  [11,23,45,74,23,56,2,4]
# print(my_list[0])
# print(my_list[-1])


# slicing : 
# print(my_list[:])
# print(my_list[::])
# print(my_list[1:])
# print(my_list[1:3])
# my_list =  [11,23,45,74,23,56,2,4]

# print(my_list[1:5:2])

# print(my_list[-1:-5:-1])


# 
# my_list =  [11,23,45,74,23,56,2,4]
# print(my_list)

# my_list.append("Raj")
# print(my_list)

# my_list.append("Raj")
# print(my_list)

# my_list.append(("Raj","Rahul"))
# print(my_list)

# my_list.extend(["Raj","Rahul"])
# print(my_list)


# new_list = my_list.copy()
# print(new_list)

# new_list_2 = my_list 
# print(new_list_2)

# print(id(my_list))
# print(id(new_list))
# print(id(new_list_2))


# num1 = 12

# num2 = num1

# num1 = 11

# print(num1,num2)
# print(id(num1),id(num2))

# num3 = 11
# print(num3,id(num3))


# my_list =  [11,23,45,74,23,56,2,4]
# print(my_list)

# my_list.count  return : element 
# my_list.index

# my_list.insert(3,12)
# print(my_list)


# my_list.insert(-3,12)
# print(my_list)


# my_list.pop(3)
# print(my_list)

# my_list.remove(23)
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)

# my_list.reverse()

# print(my_list)

# my_list.clear()

# del my_list
# print(my_list)

# my_list =  [11,23,45,74,23,56,2,4]

# del my_list[3]

# print(my_list)


# Type Casting : 

my_tuple = (1,2,34,4)
print(my_tuple)
# del my_tuple[1]
# print(my_tuple)

my_list = list(my_tuple)
print(my_list)
del my_list[1]
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)





