import itertools as it

a,b,c = map(int,input().split())
k = int(input())

allcase = list(it.product([0,1,2,3],repeat=k))

for case in allcase:
  nums = [a,b,c]
  for step in case:
    if step == 3:
      continue
    nums[step] *= 2
  if nums[0] < nums[1] and nums[1] < nums[2]:
    print('Yes')
    exit()
print('No')