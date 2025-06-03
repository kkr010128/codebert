from itertools import combinations

N = int(input())
L = list(map(int, input().split()))

ans = 0
for i, j, k in combinations(range(N),3):
  ell = sorted([L[i], L[j], L[k]])
  if ell[2] < ell[0] + ell[1] and len(set(ell)) == 3:
    ans += 1
print(ans)