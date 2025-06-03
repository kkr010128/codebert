n=int(input())
r=list(map(int,input().split()))
s=0
for u in r: s^=u
t=[x ^ s for x in r]
print(*t)