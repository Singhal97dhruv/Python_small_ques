# Write a program to take age from user and check whether it will be able to vote.If not then print after how many years it will be able to vote
age=int(input("Enter your age: "))
if age>=18:
    print("Yes you are eligible for voting")
else:
    print("Sorry! You can't vote.You are eligible for voting after "+str(18-age)+" years")