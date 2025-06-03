N = int(input())
L = []
for i in range(N):
  L.append(list(input().split()))
S = input()
ans = 0
f = 0
for i in range(N):
  if f == 1:
    ans += int(L[i][1])
  if L[i][0] == S:
    f = 1
print(ans)