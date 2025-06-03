n = int(input())
l = list(map(int,input().split()))
p=l[0]
s=0
for i in l[1:]:
    s+= max(0,p-i)
    p=max(p,i)
print(s)