n = int(input())
a = ["a","b","c","d","e","f","g","h","i","j"]
def dfs(s):
  m = len(s)
  if m == n:
    ans = ""
    for i in range(n):
      ans += a[int(s[i])]
    print(ans)
  else:
    for i in range(int(max(list(s)))+2):
      dfs(s+str(i))

dfs("0")