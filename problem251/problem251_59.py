N,K = map(int,input().split())
R,S,P = map(int,input().split())
dp = []
order = input()
def jcount(x):
  if x=='r':
    ans = P
  elif x=='s':
    ans = R
  else:
    ans = S
  return ans
counter = 0
for i in range(N):
  if i < K:
    counter += jcount(order[i])
    dp.append(order[i])
  elif order[i] != dp[i-K]:
    counter += jcount(order[i])
    dp.append(order[i])
  else:
    dp.append('x')
print(counter)