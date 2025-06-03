x, n = list(map(int, input().split()))
if n == 0:
  inputs = []
else:
  inputs = list(map(int, input().split()))
nums = [0] * 201
diff = 1000
n = 100
for i in inputs:
  nums[i] = 1
for i in range(0, 201):
  d = abs(i - x)
  if nums[i] == 1:
    continue
  if d < diff:
    diff = d
    n = i
print(n)
