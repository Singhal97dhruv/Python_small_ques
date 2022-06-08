# Write a python program to print square and cubes of numbers
n =int(input("Enter any number: "))
print("Number"+"\t"+"Square"+"\t"+"Cube")
for i in range(1,n+1):
    print(i,"\t",i*i,"\t",i*i*i)
