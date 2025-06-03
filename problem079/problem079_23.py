s = int(input())
a = [None, 0, 0] + [1] * (s - 2)
for i in range(3, s - 2):
  a[i + 3] += a[i]
  a[i + 1] += a[i]
print(a[s] % (10**9 + 7))
