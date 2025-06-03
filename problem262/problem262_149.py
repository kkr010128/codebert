# bit全探索 典型といえば典型（問題文の意味がよくわからんので読解力コンテスト）

n = int(input())
syogen = []
for i in range(n):
    syogen.append([])
    for _ in range(int(input())):
        syogen[i].append(list(map(int, input().split())))

ans = 0
for bit in range(1 << n):
    p = ["不親切"] * n
    ng = False
    # bitの立っているのを正直者と仮定
    for i in range(n):
        if bit >> i & 1 == 1:
            # 上位bit = 小さいインデックス、になる（ように実装してしまった わかりづらい
            p[n - i - 1] = "正直者"
    for i in range(n):
        if p[i] == "不親切":
            # まあ不親切な人間のことなんて聞かなくていい
            continue
        for s in syogen[i]:
            if p[s[0] - 1] == "正直者" and s[1] == 1:
                # 証言と一致する
                continue
            elif p[s[0] - 1] == "不親切" and s[1] == 0:
                # 証言と一致する
                continue
            else:
                # 証言と一致しない
                ng = True
                break

    if not ng:
        ans = max(ans, p.count("正直者"))
print(ans)
