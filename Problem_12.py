# Write a program to print this pattern
# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()
n=5*2-2  # no of spaces
for i in range(5):
    for j in range(n):
        print(end=" ")
    n=n-2
    for j in range(i+1):
        print("* ",end="")
    print()