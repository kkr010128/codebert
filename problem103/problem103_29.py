import sys
readline = sys.stdin.readline

# 常に金額で持ち、明日のほうが上がるときのみ、必ず買って売るを繰り返す

N = int(readline())
A = list(map(int,readline().split()))

money = 1000
for i in range(N - 1):
  if A[i] < A[i + 1]:
    kabu = money // A[i]
    money %= A[i]
    money += kabu * A[i + 1]
    
print(money)