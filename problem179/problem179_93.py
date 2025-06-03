import math
N, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
th = math.ceil(S / (4*M))

ans = 0
for a in A:
  if a >= th:
    ans += 1
    
print("Yes" if ans >= M else "No")
  
