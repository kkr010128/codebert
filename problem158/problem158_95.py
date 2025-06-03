k = int(input())
a, b = map(int, input().split())
check = False
for i in range(a, b + 1):
  if i % k == 0:
    check = True
print("OK" if check else "NG")