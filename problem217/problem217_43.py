n=int(input())

a=list(map(int,input().split()))

t=1

for i in range(n):
    if a[i]%2==0 and a[i]%3==0:
        t=1
    elif a[i]%2==0 and a[i]%5==0:
        t=1
    elif a[i]%2==1:
        t=1
    else:
        t=0
        break 

if t==1:
    print("APPROVED")
else:
    print("DENIED")
