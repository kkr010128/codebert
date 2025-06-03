n = int(input())
L = list(map(int, input().split()))
L.sort()
count = 0
for i in range(n - 2):
  a = L[i]
  for j in range(i + 1, n - 1):
    b = L[j]
    l = j
    r = n
    while r - l > 1:
      p = (l + r) // 2
      if L[p] < a + b:
        l = p
      else:
        r = p
    count += l - j
print(count)
