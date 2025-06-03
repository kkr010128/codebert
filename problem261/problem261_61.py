s = input()
rs = s[::-1]
ans = 0
for i in range(len(s)//2):
  ans += (s[i] != rs[i])
print(ans)