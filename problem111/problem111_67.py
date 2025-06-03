n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
cnt = 0
for i in range(1, n):
  cnt += a[i // 2]
print(cnt)