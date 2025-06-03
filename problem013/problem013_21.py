N = int(input())
R = [int(input()) for _ in range(N)]

p_buy = R[0]
p_sale = R[1]
buy = R[1]
sale = None
for i in range(2, N):
    if p_sale < R[i]:
        p_sale = R[i]
    if buy > R[i]:
        if sale is None:
            sale = R[i]
        if p_sale - p_buy < sale - buy:
            p_sale, p_buy = sale, buy 
        sale, buy = None, R[i]
    else:
        if sale is None or sale < R[i]:
            sale = R[i]

p_gain = p_sale - p_buy
print(p_gain if sale is None else max(p_gain, sale - buy))