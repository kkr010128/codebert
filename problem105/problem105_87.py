n = int(input())
a = 0
l = list(map(int, input().split()))
for i in range(n):
  if i % 2 == 0:
    if l[i] % 2 != 0:
      a = a + 1
print(a)