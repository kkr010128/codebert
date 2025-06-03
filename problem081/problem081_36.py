# 入力
D, T, S = input().split()

# 以下に回答を記入
D = int(D)
T = int(T)
S = int(S)

if T * S >= D:
  print('Yes')
else:
  print('No')