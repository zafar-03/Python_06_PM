# def cube(mylist):
    # for element in mylist:
        # print(element*element*element)
        # print(element**3)
        # print(pow(element,3))

# cube([1,2,3,4])



# def freq(mystr):
#     mydict = {}
#     for char in mystr:
#         mydict.update({char : mystr.count(char)})

#     return mydict


# print(freq("welcome to Python."))



# 0,1,1,2,3,5,8,13,21,34,55......
# a+b
#     c
#   a+b
#       c


def fibonacci(n):
    """
     0,1,1,2,3,5,8,13,21,34,55......
     a+b
         c
       a+b
           c
    """
    a = 0
    b = 1
    for i in range(0,n):
        print(a,end=",")
        c = a+b 
        a = b
        b = c 

fibonacci(10)

print(fibonacci.__doc__)