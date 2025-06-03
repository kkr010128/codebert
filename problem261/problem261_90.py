S = input()

result = 0
# 入力例1なら3文字目まで
for i in range(len(S) // 2):
  # sの1(2番目)がsの最後尾と一緒ならカウント
  if S[i] != S[-(i + 1)]:
    result += 1
print(result)