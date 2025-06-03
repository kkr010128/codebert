from math import floor

S = input()
K = int(input())

# Sが1文字しかない
if len(set(S)) == 1:
    print(floor(len(S) * K / 2))
    exit()

ans = 0
if S[0] != S[-1]:
    # Sの中での答え × K回数
    c = "0"
    count = 0
    for i in range(len(S)):
        if c == S[i]:
            count += 1
        else:
            # floor(連続した文字の回数 / 2)だけ書き換える
            ans += count // 2
            c = S[i] # 情報更新
            count = 1
    ans += count // 2 # 最後の分
    ans = ans * K
else:
    # 先頭と末端もある
    c1 = 1
    for i in range(1, len(S)):
        if S[i] == S[0]:
            c1 += 1
        else:
            break
    c2 = 1
    for j in reversed(range(len(S) - 1)):
        if S[j] == S[-1]:
            c2 += 1
        else:
            break
    ans = (c1 // 2) + (c2 // 2) + ((c1 + c2) // 2 * (K - 1))
    c3 = 0
    c = "0"
    for k in range(i, j + 1):
        if S[k] == c:
            c3 += 1
        else:
            ans += c3 // 2 * K
            c = S[k]
            c3 = 1
    ans += c3 // 2 * K
print(ans)