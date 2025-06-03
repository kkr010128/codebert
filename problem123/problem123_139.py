N = int(input())
A = list(map(int, input().split()))
x = 0
ans = list()
for ai in A:
  x = x ^ ai
for ai in A:
  ans.append(x ^ ai)
print(*ans)