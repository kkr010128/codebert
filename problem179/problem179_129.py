n,m=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
a.sort(reverse=True)
ALL=0

for i in a:
    ALL+=i


for i in range(m):
    if a[i]>=ALL/(4*m):
        cnt+=1
        if cnt==m:
            print("Yes")
    else:
        print("No")
        break
