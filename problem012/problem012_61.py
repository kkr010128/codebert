import pdb

n = int(raw_input())
count = 0
for x in xrange(n):
  target = int(raw_input())
  # pdb.set_trace()
  if target == 2:
    count += 1
  elif target < 3 or not target & 1:
    continue
  else:
    if pow(2, target - 1, target) == 1:
      count += 1

print count