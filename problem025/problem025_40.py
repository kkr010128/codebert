N = int(input())
A = list(map(int,input().split()))
Q = int(input())
M = list(map(int,input().split()))


def bitsearch():
  nums = [0] * (2 ** N)
  for i in range(2 ** N):
    num = 0
    for j in range(N):
      if (i >> j) & 1:
        num += A[j]
        nums[i] = num
  for q in range(Q):
    if M[q] in nums:
      print("yes")
    else:
      print("no")

bitsearch()

