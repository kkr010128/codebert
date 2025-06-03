n = int(input())
def dfs(s):
  if len(s) == n:
    print(s)
  else:
    max_list = []
    for _ in s:
      max_list.append(ord(_))
    for i in range(ord("a"),max(max_list) + 2):
      s = s + chr(i)
      dfs(s)
      s = s[:len(s) - 1]
      
dfs("a")