num = 5

print("Ptn 1 :")
for i in range(0,num):
    for j in range(0,num):
        print("* ",end="")
    print()

print("Ptn 2 :")
for i in range(0,num):
    for j in range(0,i+1):
        print("* ",end="")
    print()

print("Ptn 3 :")
for i in range(0,num):
    for j in range(0,i+1):
        print(i,end=" ")
    print()

print("Ptn 4 :")
for i in range(0,num):
    for j in range(0,i+1):
        print(j,end=" ")
    print()

k=0
print("Ptn 5 :")
for i in range(0,num):
    for j in range(0,i+1):
        print(k,end=" ")
        k+=1
    print()



print("Ptn 5 :")
for i in range(0,num):
    for j in range(0,i+1):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()

print("Ptn 6 :")
for i in range(0,num):
    for j in range(0,i+1):
        if i%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()

k=1
print("Ptn 7 :")
for i in range(0,num):
    for j in range(0,i+1):
        if i%2==0:
            print(k,end=" ")
        else:
            print("*",end=" ")
        k+=1
    print()

print("Ptn 8 :")
for i in range(0,num):
    for j in range(0,i+1):
        if i==j:
            print(0,end=" ")
        else:
            print(i,end=" ")
    print()



print("Ptn 9 :")
for i in range(0,num):
    k=num
    for j in range(0,i+1):
        print(k,end=" ")
        k-=1
    print()