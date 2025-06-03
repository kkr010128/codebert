n, m= map(int, input().split())
ans = [10] * (n + 1)
#s-digit: ans = [dummy, 1st-d, 2nd-d, ...]
for i in range(m):
  s, c = map(int, input().split())
  if ans[s] == 10 and not (n!=1 and s==1 and c==0):
    ans[s] = c
  elif ans[s] == c:
    pass
  elif ans[s] != c or (n!=1 and s==1 and c==0):
    print(-1)
    exit()
for i in range(1, n+1):
  if ans[i] == 10:
    ans[i] = 0
    if i == 1 and n != 1:
      ans[i] += 1
print(''.join([str(x) for x in ans[1:]]))