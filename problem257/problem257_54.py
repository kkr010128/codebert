N=int(input())
A=list(map(int,input().split()))
count=0
num=1
for i in range(N):
    if A[i]==num:
        count+=1
        num+=1

if count==0:
    print(-1)
else:
    print(N-count)