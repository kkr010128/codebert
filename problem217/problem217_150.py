n = int(input())
l = list(map(int, input().split()))
c = 0
for i in l:
  if i%2 == 0:
    if i%3 != 0 and i%5 != 0:
      c += 1
      break
print("DENIED" if c > 0 else "APPROVED")