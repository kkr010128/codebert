n, k, s = map(int, input().split())

ans = []
for i in range(k):
  ans.append(s)

if s == pow(10, 9):
  s = 0
  
for j in range(k, n):
  ans.append(s+1)
  
print(' '.join(list(map(str, ans))))