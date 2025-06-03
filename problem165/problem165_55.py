import collections
n=int(input())
box=[]
for i in range(n):
    tmp=str(input())
    box.append(tmp)
l=len(collections.Counter(box))
print(l)