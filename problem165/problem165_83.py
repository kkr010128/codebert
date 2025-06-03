n=int(input())
l=[]
for i in range(n):
    s=str(input())
    l.append(s)
k=set(l)
print(len(k))