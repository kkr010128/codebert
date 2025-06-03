def solve(n,s):
  if "ABC" not in s:
    return 0
  cnt = 0
  for i in range(len(s)-2):
    if "ABC" == s[i:i+3]:
      cnt+=1
  return cnt

n = int(input())
s = input()
ans = solve(n,s)
print(ans)
