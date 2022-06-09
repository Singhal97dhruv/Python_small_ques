# Write a program to calculate union of two sets
list1=[]
list2=[]
n1=int(input("Enter the number of elements you want to enter in list1: "))
n2=int(input("Enter the number of elements you want to enter in list2: "))
print("Enter numbers for list 1:")
for i in range(n1):
    list1.append(int(input()))
print("Enter numbers for list 2:")
for i in range(n2):
    list2.append(int(input()))
list3=list1+list2
print("Union of two lists are "+str(list3)+"")