def swap_pos(list,pos1,pos2):
    list[pos1-1],list[pos2-1]=list[pos2-1],list[pos1-1]

def swap_pos2(list,pos1,pos2):
    get=list[pos1-1],list[pos2-1]
    list[pos2-1],list[pos1-1]=get

l=[1,2,3,4,5,6,7]
pos1,pos2=1,3
print("list before swapping")
print(l)
swap_pos2(l,pos1,pos2)
print("list after swapping")
print(l)

