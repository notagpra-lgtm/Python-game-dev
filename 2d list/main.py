# list1=["ice cream","chocolate","tiramisu","cake","candy"]
# print(list1[1])
 
# list2=[
#     [1,2,3,4],
#     ["A","B","C","D"],
#     ["+","*","&","?"],
#     [9,10,11,12]
# ]
# print(list2[2][2])

# list3=[ 
#     [1,2,3],
#     ["A","B","C"],
#     ["+","*","&"]
# ]
# for r in list3:
#     for c in r:
#         print(c,end="")
#     print()


print("Welcome to the name management system!\nHere you can\n1.Add a name\n2.View all names\n3.Remove the name\n4.Exit")
namelist=[ ]
option=int(input("How would you like to proceed? "))
if option==1:
    name=input("Please enter the name: ")
    namelist.append(name)
    print("Your name has been added")