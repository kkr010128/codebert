import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))
DIV = 10 ** 9 + 7

# 各桁の1と0の数を数えて、((1の数) * (0の数)) * (2 ** i桁目(1桁目を0とする))を数える

K = max(A) # 最も大きい数が0になるまでループ
ans = 0
j = 0
while K:
  one = 0
  for i in range(len(A)):
    if (A[i] >> j) & 1:
      one += 1
  ans += (one % DIV) * ((N - one) % DIV) * pow(2,j,DIV)
  ans %= DIV
  j += 1
  K >>= 1
  
print(ans)