n=int(input())
a=0
for _ in range(n):
    x,y=map(int,input().split())
    if x==y:
        a+=1
    else:
        a=0
    if a==3:
        print("Yes")
        exit(0)
print("No")
