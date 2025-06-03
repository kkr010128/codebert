n=int(input())
a=[0]+list(map(int,input().split()))
b=[0 for i in range(n+1)]

for i in range(n):
    b[a[i]]+=1

[print(i) for i in b[1:]]
