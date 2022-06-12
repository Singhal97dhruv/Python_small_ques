#Python problem to get 3 nos and put in eqn a+b+ca/b(2a+3b)
a,b,c=int(input("Enter first number: ")),int(input("Enter second number: ")),int(input("Enter third number: "))
print("Result is:",(a+b+c)*(a/b)*(2*a+3*b))