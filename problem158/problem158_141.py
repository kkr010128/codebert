n = int(input())
a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
  if i % n == 0:
    ans += 1
    break
print("OK" if ans == 1 else "NG")