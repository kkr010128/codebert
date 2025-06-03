# 入力
a = int(input())

# 定義
answer = 0

# 処理
for i in range(1, a + 1):
    if i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    else:
        answer += i

# 出力
print(answer)
