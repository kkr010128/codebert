ans = 0
n = 0
h = int(input())

while h != 1:
  h = h//2
  n += 1
for i in range(n + 1):
  ans = ans + 2 ** i
print(ans)