A = [0] * 9
nums = dict()
for i in range(3):
  temp = list(map(int, input().split()))
  for j, var in enumerate(temp):
    nums[var] = i * 3 + j
N = int(input())

for _ in range(N):
  i = int(input())
  if i in nums:
    A[nums[i]] = 1

bingo = [
  A[0] + A[1] + A[2],
  A[3] + A[4] + A[5],
  A[6] + A[7] + A[8],
  A[0] + A[3] + A[6],
  A[1] + A[4] + A[7],
  A[2] + A[5] + A[8],
  A[0] + A[4] + A[8],
  A[2] + A[4] + A[6]]

if 3 in bingo:
  print("Yes")
else:
  print("No")
