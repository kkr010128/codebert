r=input().split()
X=int(r[0])
Y=int(r[1])
ans=0
for i in range(X+1):
    if 2*i==4*X-Y:
        print("Yes")
        ans+=1
        break
if ans==0:
    print("No")