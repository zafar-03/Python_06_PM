# def cube(n):
#     print(n**3)
# cube(11)

# Anonymous / lambda function:
"""
Syntax : 

lambda variable : operation

"""
# cube = lambda n : n**3


# print(cube(11))


# cube = lambda n : print(n**3)

# cube(11)




mylist = [2,56,7,34,66,3,55,1]

print(mylist)

# print(sorted(mylist))
# print(sorted(mylist,reverse=True))


# print(sorted(mylist,key= lambda x : x))

print(list(map(lambda x : x**3,mylist)))
print(list(filter(lambda x : x > 40,mylist)))
