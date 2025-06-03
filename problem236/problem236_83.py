H=int(input())
W=int(input())
N=int(input())
K=H
if K<W: K=W
sum = 0
ans= 0
for i in range(1,K+1):
  if sum < N:
    sum += K
    ans = i
    #print(ans, K)
print(ans)