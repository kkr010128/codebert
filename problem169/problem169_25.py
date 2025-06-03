n = int(input())
a = list(map(int,input().split()))
ans = {i:0 for i in range(n)}
for i in a:
  ans[i-1] += 1

for i in ans.values():
  print(i)