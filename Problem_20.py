#Python program to take 5nos from user in array and sum all that
import array as a
arr=a.array('i',[])
sum=0
for i in range(5):
    arr.append(int(input("Enter the number: ")))
for j in range(5):
    print(arr[j])
    sum+=arr[j]
print("Sum of the entered numbers is",sum)
print("Maximum number is :",max(arr))
print("Minimum number is :",min(arr))
