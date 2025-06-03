def solution(arr):
  count = 0
  for i, j in arr:
    if i == j:
      count += 1
    else:
      count = 0
    if count == 3:
      return 'Yes'
  return 'No'
n = int(input())
arr = []
for _ in range(n):
  arr.append([ int(i) for i in input().split()])
print(solution(arr))