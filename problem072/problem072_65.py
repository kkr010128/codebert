n=int(input())
rec=[False]*n
for i in range(n):
    a,b=map(int,input().split())
    if a==b:
        rec[i]=True
for i in range(n-2):
    if rec[i] and rec[i+1] and rec[i+2]:
        print("Yes")
        exit()
print("No")