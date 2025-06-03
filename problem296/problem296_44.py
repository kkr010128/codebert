S = str(input())
K = int(input())

li = []
cnt = 1
for i in range(len(S)-1):
  if S[i] == S[i+1]:
    cnt += 1
  else:
    li.append(cnt)
    cnt = 1
li.append(cnt)
  
ans = 0
first = li[0]
last = li[-1]
if (S[0]==S[-1]) and (len(li)>1):
  li[-1] += first
  li.pop(0)
  for l in li:
    ans += l // 2
  ans *= K
  ans -= li[-1] // 2
  ans += first//2 + last//2
elif S[0] == S[-1]:
  ans = li[0] * K // 2
else:
  for l in li:
    ans += l // 2
  ans *= K
print(ans)