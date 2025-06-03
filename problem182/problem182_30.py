def solve():
  N, K, C = map(int, input().split())
  workable = [i for i, s in enumerate(input(), 1) if s=="o"]
  
  if len(workable) == K:
    return workable
  
  latest = set()
  prev = workable[-1]+C+1
  for x in reversed(workable):
    if prev - x > C:
      latest.add(x)
      prev = x
  
  if len(latest) > K:
    return []
  
  def ans():
    prev = -C-1
    for x in workable:
      if x - prev > C:
        if x in latest:
          yield x
        prev = x
  return ans()

print("\n".join(map(str, solve())))
