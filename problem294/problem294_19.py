from bisect import bisect_left

N = int(input())
Lli = list(map(int,input().split()))

Lli.sort()

res = 0

for i in range(N-2):
  for j in range(i+1,N-1):
    ab = Lli[i]+Lli[j]
    res += bisect_left(Lli,ab)-j-1
    
print(res)