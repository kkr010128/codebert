n, k = map(int, input().split())
a_nums = list(map(int, input().split()))

f_point = sum(a_nums[:k])
for i in range(n - k):
  if a_nums[i] < a_nums[i + k]:
    print("Yes")
  else:
    print("No")