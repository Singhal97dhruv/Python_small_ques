l=[3,4,5,6,7,8,99,33,2,222,11]
# print("Enter the number of elements you want in list")
# n=int(input())
# print("Enter elements in list")
# for i in range(n):
#     ele=int(input())
#     l.append(ele)
print("The list is: "+str(l))
occ=0
for i in l:
    occ=occ+1
print("The length of list is "+str(occ))

#Or use builtin
print(len(l))