def tax_increase():
    """
    消費税率 8% → 消費税 A円
    消費税率 10% → 消費税 B円
    商品価格 X = A / 0.08  → 25A / 2
        　　 X = B / 0.1   → 10B
    消費税は切り捨てなので、消費税の範囲は
    A <= X < A+1
    """
    # 入力
    A, B = map(int, input().split())
    # 初期処理
    tax_excluded_price_list1 = list()
    tax_excluded_price_list2 = list()
    # 消費税率 8%
    tax_excluded_price_low1 = 25 * A / 2 # 税抜き価格1
    tax_excluded_price_low2 = int(tax_excluded_price_low1) # 小数点以下切り捨て1
    tax_excluded_price_high1 = 25 * (A+1) / 2 # 税抜き価格2
    tax_excluded_price_high2 = int(tax_excluded_price_high1) # 小数点以下切り捨て2
    # 税抜き価格の取り得る範囲 
    for i in range(tax_excluded_price_low2, tax_excluded_price_high2+1):
        if tax_excluded_price_low1 <= i and i < tax_excluded_price_high1:
            tax_excluded_price_list1.append(i)
    # 消費税率 10%
    tax_excluded_price_low1 = 10 * B # 税抜き価格1
    tax_excluded_price_low2 = int(tax_excluded_price_low1) # 小数点以下切り捨て1
    tax_excluded_price_high1 = 10 * (B+1) # 税抜き価格2
    tax_excluded_price_high2 = int(tax_excluded_price_high1) # 小数点以下切り捨て2
    # 税抜き価格の取り得る範囲 
    for i in range(tax_excluded_price_low2, tax_excluded_price_high2+1):
        if tax_excluded_price_low1 <= i and i < tax_excluded_price_high1:
            tax_excluded_price_list2.append(i)
    # 最も小さい金額で条件を満たすもの
    for i in tax_excluded_price_list1:
        if i in tax_excluded_price_list2:
            return i
    # 条件を満たす税抜き価格がない場合
    return '-1'
    
result = tax_increase()
print(result)