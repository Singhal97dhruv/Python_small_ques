# Write a python program to calculate intersection of two sets
set1={2,3,5,6,10,11,12,14}
set2={2,3,22,6,9,10,50}
# n1=int(input("Enter the number of elements you want in set1: "))
# n2=int(input("Enter the number of elements you want in set2: "))
# for i in range(n1):
#     set1.add(int(input()))
# for i in range(n2):
#     set2.add(int(input()))
# print(set1)
# print(set2)
set3=set1.intersection(set2)
print(set3)

# Python program to calculate intersection of three sets
set4={2,3,56,65,48,79,14}
print(set4.intersection(set1,set2))