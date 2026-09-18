# Tuple : 
# It's Collection of Data which is same of Different Datatype.
# Not Changable
# Ordered
# Index : Available

"""
Syntax : 
1. Empty Tuple :
variable_name = ()



2. Tuple with data :
variable_name = (11,23,45)
variable_name = ("Raj","sahil")
variable_name = (11,23,"Raj",True,3.14)

3. Tuple with Single Value :
variable_name = (value,)
variable_name = value,
variable_name = value,value2,....

4. variable_name = tuple()
"""

# my_tuple = ()
# print(my_tuple)
# print(type(my_tuple))


# my_tuple = (11,12,13)
# my_tuple = (11,12,13,"Raj")
# my_tuple = ("sahil","Raj")


# print(my_tuple)
# print(type(my_tuple))


# my_tuple = ("Raj",)


# print(my_tuple)
# print(type(my_tuple))


# my_tuple = 12,13,14,15


# print(my_tuple)
# print(type(my_tuple))


# my_tuple = tuple()

# print(my_tuple,type(my_tuple))

# my_tuple = tuple([11,12,13,14,15,5,6,7,84,3])
# my_tuple = tuple({11,12,13,14,15,5,6,7,84,3})
# my_tuple = tuple("11,12,13,14,15,5,6,7,84,3")

# my_tuple = (11,12,13,14,15,5,6,7,84,3,56,78)
#            0  1  2  3  4 5 6 7  8 9

# print(my_tuple,type(my_tuple))


# Access All The Element(value) one by one
#1.  Using a Loop :
# for element in my_tuple:
#     print(element)

# for index in range(0,10):
#     print(my_tuple[index])

# Methods : 

# len() : length method (global method) :
# print(len(my_tuple))
# for index in range(0,len(my_tuple)):
#     print(my_tuple[index])

my_tuple = (11,12,13,1,15,5,6,7,84,3,56,1,78,1)

# my_tuple[0] = 100
# print(my_tuple)


# 1. count:
# print(my_tuple.count(190))

# 2. index:
# print(my_tuple.index(560))



# Operators : 
# in
# not in

# print(12 not in my_tuple)
# num = 190
# if num in my_tuple:
#     print("Index is :",my_tuple.index(num))
# else:
#     print("Number Doesn't Exist")


# my_tuple.