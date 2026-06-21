def obj(x):
    return -(x-5)**2+25
curr=0
while True:
    left=curr-1
    right=curr+1
    if obj(left)>obj(curr):
        curr=left
    if obj(right)>obj(curr):
        curr=right
    else:
        break
print("best solution",curr)
print("max vaue",obj(curr))