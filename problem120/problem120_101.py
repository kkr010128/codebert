a, nums = map(int, input().split())
add = 0
lst = list(map(int, input().split()))
lst.sort()
for i in range(0,nums):
  add += lst[i]

print(add)