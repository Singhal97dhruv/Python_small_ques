l=[]

n=int(input("Enter number of elements: "))
for i in range(n):
    ele=int(input())
    l.append(ele)
print(l)
# Now after interchanging

# 1st approach
# ele=l[0]
# l[0]=l[-1]
# l[-1]=ele

# 2nd approach
get=l[0],l[-1]
l[-1],l[0]=get

print(l)