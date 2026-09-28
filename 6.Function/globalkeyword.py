# num = 11

# def greeting():
#     global num
#     num = 100
#     print("Inner Answer :",num)

# greeting()

# print("Outer Answer :",num)
# =================================
num = 11

def greeting():
    global num
    num += 100
    print("Inner Answer :",num)

greeting()

print("Outer Answer :",num)