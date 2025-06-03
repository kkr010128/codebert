n, k = map(int, input().split())
a = list(map(int, input().split()))
b = 0
for i in (a):
  if i >= k:
    b += 1
  else:
    b += 0
print(b)