N = int(input())
s = "a"
ans = []
def dfs(s,n):
  if len(s) == n:
    ans.append(s)
    return
  last = 0
  for i in range(len(s)):
    last = max(last,ord(s[i]))
  limit = chr(last+1)
  for i in range(26):
    temp = chr(97+i)
    if temp <= limit:
      dfs(s+temp,n)
dfs(s,N)
print(*ans,sep="\n")