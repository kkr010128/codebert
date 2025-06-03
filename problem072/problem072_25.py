n = int(input())
cnt=0
for _ in range(n):
    a,b=map(int,input().split())
    if a==b:
        cnt+=1
        if cnt>=3:
            break
    else:
        cnt=0
if cnt>=3:
    print("Yes")
else:
    print("No")