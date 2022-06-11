# Python program to get 6 nos in list and sum that nos 
list=[]
for i in range(6):
    list.append(int(input("Enter "+str(i+1)+"th number: ")))
sum=0
for i in range(6):
    sum+=list[i]
print("Sum of numbers present in list are: ",sum)