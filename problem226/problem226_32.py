n,d=list(map(int,input().split()))
s=list(map(int,input().split()))
v=0
for i in s:
    v+=int(i)
if v>=n:
    print("Yes")
else:
    print("No")
