N, M = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)

ans = 0
for a in A:
  if a * 4 * M >= s:
    ans += 1

print("Yes" if ans >= M else "No")
