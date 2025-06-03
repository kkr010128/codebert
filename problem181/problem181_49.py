from collections import deque
K = int(input())
nums = deque([])
for i in range(1, 10):
  nums.appendleft(i)
count = 1
while count < K:
  num = nums.pop()
  last = int(str(num)[-1])
  for i in range(max(0, last-1), min(10, last+2)):
    nums.appendleft(int(str(num)+str(i)))
  count += 1
print(nums.pop())
