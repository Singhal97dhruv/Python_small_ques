# Python program to get 6 number in the list and display all number all number and then clear the list and then display 
list=[]
for i in range(6):
    list.append(int(input("Enter "+str(i+1)+"th number: ")))
print(list)
list.clear()
print(list)