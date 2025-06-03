a, b = [int(i) for i in input().split()]
ans = -1
for i in range(1010):
  if i * 8 // 100 == a and i // 10 == b:
    ans = i
    break
print(ans)