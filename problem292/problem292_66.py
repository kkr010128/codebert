N=int(input())
d=list(map(int,input().split()))

a=0
for i in range(N):
    for k in range(1,N-i):
        a=a+d[i]*d[i+k]
print(a)