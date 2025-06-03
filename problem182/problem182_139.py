def solve():
  N, K, C = map(int, input().split())
  workable = [i for i, s in enumerate(input()) if s=="o"]
  if len(workable) == K:
    return workable
    
  prev = workable[-1]
  latest = {prev}
  i = len(workable)-1
  while i > 0:
    i -= 1
    if prev - workable[i] > C:
      latest.add(workable[i])
      prev = workable[i]
      if len(latest) > K:
        return []
  must = []
  i = -1
  prev = -C-1
  while i < len(workable)-1:
    i += 1
    if workable[i] - prev > C:
      if workable[i] in latest:
        must.append(workable[i])
      prev = workable[i]
  return must

for i in solve():
  print(i+1)