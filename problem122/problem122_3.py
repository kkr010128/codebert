N = int(input())
A = list(map(int, input().split()))
A_MAX = 10 ** 5
idx = [0] * (A_MAX + 1)
sum = 0
for i in A:
  idx[i] += 1
  sum += i
Q = int(input())
for i in range(Q):
  B, C = list(map(int, input().split()))
  sub = C - B
  num = idx[B]
  idx[B] = 0
  idx[C] += num
  sum += (sub * num)
  print(sum)