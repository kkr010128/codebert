from collections import defaultdict

N=int(input())
count=defaultdict(int)
*A,=map(int,input().split())
for i in range(N):
  count[A[i]] += 1
  
ans = 0
for k in count.keys():
  ans += count[k]*k

Q=int(input())
for q in range(Q):
  b,c = map(int,input().split())
  ans += c*count[b] - b*count[b]
  count[c] += count[b]
  count[b] = 0
  print(ans)