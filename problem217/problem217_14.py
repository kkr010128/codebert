n=int(input())
a=list(map(int,input().split()))
b=[]
f=1
for i in a:
    if i%2==0:
        b.append(i)
for j in b:
    if not (j%3==0 or j%5==0):
        f=0
if f:
    print("APPROVED")
else:
    print("DENIED")