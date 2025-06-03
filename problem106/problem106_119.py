n = int(input())

nums = [0]*n
a = int(n**0.5)+1
for x in range(1,a):
  for y in range(1,a):
    if x**2 + y**2 + x*y > n: break
    for z in range(1,a):
      s = x**2 + y**2 + z**2 + x*y + y*z + z*x
      if s <= n: nums[s-1] += 1
print(*nums, sep="\n")