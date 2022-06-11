# Python program to get password from user and validate that password should contain numeric and alphabetic and password length should be less than 8
s=input("Generate a password : ")
if(s.isalnum() and len(s)<8):
    print("Password valid")
else:
    print("Password invalid")