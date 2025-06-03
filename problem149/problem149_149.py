n, m, x = list(map(int, input().split()))
books = []
for _ in range(n):
    books.append(list(map(int, input().split())))

# 参考書の組み合わせ
price_min = pow(10, 6) * n
found = False
for bits in range(2 ** n):
    level = [0] * m
    price = 0
    # ビットが立っている参考書の理解度と値段を加算
    for book in range(n):
        if (bits >> book) & 1:
            price += books[book][0]
            for alg in range(m):
                level[alg] += books[book][alg + 1]
    # 理解度がXに満たないアルゴリズムを抽出
    level = list(filter(lambda lv: lv < x, level))
    # 理解度の条件を満たし、かつ合計額が最低値を下回るときに最低値を更新
    if len(level) == 0 and price < price_min:
        found = True
        price_min = price
print(price_min if found else "-1")