n, m = map(int, input().split())
Penalty = [0]*(n+1)
AC = [False]*(n+1)
correct = 0
penalty = 0
for i in range(m):
  ans = input().split()
  problem = int(ans[0])
  result = ans[1]
  if AC[problem] == False:
    if result == 'AC':
      AC[problem] = True
      correct += 1
      penalty += Penalty[problem]
    else:
      Penalty[problem] += 1
print(correct, penalty)