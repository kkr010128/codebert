N = int(input())
MOD = 10**9+7
nums = list(map(int, input().split()))
B = [0 for _ in range(60)]
for num in nums:
  for i in range(60):
    if num>>i&1:
      B[i] += 1
answer = 0
for i, b in enumerate(B):
  if b > 0:
    answer = (answer+b*(N-b)*2**i)%MOD
print(answer)
