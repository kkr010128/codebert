tc, ac, tasks = map(int, input().split())

if tasks >= (tc + ac): tc, ac = 0,0
else:
  if tc >= tasks: tc -= tasks
  else: tc,ac = 0,ac + tc - tasks


print(tc, ac)