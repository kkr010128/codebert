n = int(input())
cnt = 0
for a in range(1, n):
  cnt += ~-n//a
print(cnt)