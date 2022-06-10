#Python program to calculate difference between two sets
x=set()
y=set()
n1=int(input("Enter the number of elements you want in set1: "))
n2=int(input("Enter the number of elements you want in set2: "))
for i in range(n1):
    x.add(int(input()))
for i in range(n2):
    y.add(int(input()))
print(x.difference(y))
print(y-x)

#for symmetric difference
print("Symmetric difference ->  ",end="")
print(x^y)
