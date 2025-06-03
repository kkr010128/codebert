from collections import Counter
def solve():
  N = int(input())
  A = list(map(int, input().split()))
  c = Counter(A)
  Q = int(input())
  ans = [0]*Q
  total = sum(A)
  for i in range(Q):
    x,y = map(int, input().split())
    total += c[x]*(y-x)
    c[y] += c[x]
    c[x] = 0
    ans[i] = total
  return ans
print(*solve(),sep='\n')
