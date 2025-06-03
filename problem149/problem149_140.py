n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

# 購買する全パターンを回す
most_row_price = 10**10
for i in range(2**n):
    comb = str(bin(i)[2:]).zfill(n)
    
    # 購買パターン毎の購入金額と理解度を算出する
    money_per_pattern = [0] * n # 購買パターン毎の金額の初期化
    understanding = [0] * m # 理解度の初期化
    total_money = 0 # 合計購入金額の初期化
    for j in range(n):
        
        # 購入しないケースは除外する
        if comb[j] == '0':
            continue
            
        # 購入するケースだけ、金額算出する
        money_per_pattern[j] = ca[j][0]
        
        # 当該パターンの理解度を算出する
        for k in range(m):
            understanding[k] += ca[j][k+1]           
    total_money = sum(money_per_pattern)            

    judge_flg = 'ok'
    for j in range(m):
        if understanding[j] < x:
            judge_flg = 'ng'
    
    if judge_flg == 'ok':
        most_row_price = min(total_money, most_row_price)

if most_row_price == 10**10:
    print(-1)
else:
    print(most_row_price)