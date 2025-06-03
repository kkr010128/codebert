s = input()
t = input()
T = list(t)
sl = len(s)
tl = len(t)
ans = 10**18

for i in range((sl-tl)+1):
  cnt = 0
  S = list(s[i:i+tl])
  for a,b in zip(S,T):
    if a != b:
      cnt += 1
  if ans > cnt:
    ans = cnt
print(ans)