N, K = map(int, input().split())
nums = list(map(int, input().split()))
expect = 0
answer = 0
for i in range(N):
  if i < K:
    expect += (nums[i]+1)/2
  else:
    expect += (nums[i]+1)/2 - (nums[i-K]+1)/2
  answer = max(answer, expect)
print(answer)