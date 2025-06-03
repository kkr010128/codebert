N, M = map(int, input().split())
ans = [-1 for _ in range(N)]
if N ==1:
  ans = 0
  clis = []
  for _ in range(M):
    s, c = map(int, input().split())
    clis.append(c)
  if len(set(clis)) == 1:
    print(clis[0])
    exit()
  elif len(set(clis)) == 0:
    print(0)
    exit()
  else:
    print(-1)
    exit()
else:
  for _ in range(M):
    s, c = map(int, input().split())
    if s == 1 and c == 0:
      print(-1)
      exit()
    if ans[s-1] == c or ans[s-1] == -1:
      ans[s-1] = c
    else:
      print(-1)
      exit()

ans[0] = max(1, ans[0])
answer = ''
for k in range(N):
  if ans[k] == -1:
    answer += '0'
  else:
    answer += str(ans[k])
print(answer)
