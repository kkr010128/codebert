n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for aa in a:
  s^=aa
for aa in a:
  b.append(s^aa)
print(*b)