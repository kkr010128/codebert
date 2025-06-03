n, m, x = map(int, input().split())
books_info = []
price_info = []
for i in range(n):
    c, *a = map(int, input().split())
    books_info.append(a)
    price_info.append(c)
pattern_list = []
for j in range(2 ** n):
    tmp_list = []
    for k in range(n):
        if ((j >> k) & 1):
            tmp_list.append(k)
        else:
            pass
    pattern_list.append(tmp_list)
book_price = 10 ** 5 * 12 + 1
for pattern in pattern_list:
    # 全ての参考書を買わない=len(pattern)が0の場合はスキップする
    if len(pattern) == 0:
        continue
    is_ok = False
    price = 0
    for j in range(m):
        m_sum = 0
        price_sum = 0
        for k in pattern:
            m_sum += books_info[k][j]
            price_sum += price_info[k]
        if m_sum >= x:
            is_ok = True
        else:
            is_ok = False
            break
        price = price_sum
    if is_ok == True:
        book_price = min(price, book_price)
    else:
        pass
print(book_price if book_price != 10 ** 5 * 12 + 1 else -1)

