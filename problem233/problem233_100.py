N = int(input())
L = list(map(int, input().split()))
mi = L[0]
co = 1
for i in range(1, N):
  mi = min(L[i], mi)
  if L[i] == 1:
    co += 1
    break
  elif mi == L[i]:
    co += 1
print(co)