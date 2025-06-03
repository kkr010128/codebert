from collections import Counter
N = int(input())
A = list(map(int, input().split()))
 
c = Counter(A)
key = c.keys()
comb = 0
for i in key:
    comb += (c[i]) * (c[i]-1) // 2
 
for i in A:
    ans = comb - (c[i]-1)
    print(ans)
  
  