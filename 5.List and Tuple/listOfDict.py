my_list = [
    {"fname" : "Raj","age" : 20, "std" : 12},
    {"fname" : "Rajesh","age" : 15, "std" : 8}
]
print(my_list)

my_list.append({
    "fname" :input("Enter a Name :"),
    "age" : int(input("Enter age :")),
    "std" : int(input("Enter std :"))
})

print(my_list)



# Create(append) Read(print) Update(change) Delete(remove)