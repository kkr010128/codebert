N=int(input())
A=list(map(int,input().split()))

I=0
for a in A:
    if a==I+1:
        I+=1

if I==0:
    print(-1)
else:
    print(N-I)
