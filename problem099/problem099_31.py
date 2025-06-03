# https://atcoder.jp/contests/abc174/tasks/abc174_e

from math import ceil,floor
N,K=map(int,input().split())
A=list(map(int,input().split()))

L=0
R=max(A)
i=0
ans=(L+R)/2
cnt=0
right=0
left=0

while i<100:
    i +=1
    for num in A:
        cnt += ceil(num/ans)-1
    if cnt <=K:
        R = ans
    elif cnt>=K:
        L = ans
    else:
        #print("fin",i-1,cnt,ans)
        break           
    ans = (R+L)/2
    cnt=0
        
print(ceil(ans))