X, N = list(map(int, input().split()))
p = list(map(int, input().split()))
integer = [i for i in range(102)]
for i in range(N):
   integer.remove(p[i])
l = len(integer)
ans = -200
for i in range(l):
   if abs(ans) > abs(integer[i]-X):
      ans = integer[i] - X
print(ans + X)