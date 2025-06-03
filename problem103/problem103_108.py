N = int(input())
As = list(map(int, input().split()))

tmp = []
for i in range(1, len(As)):
    if As[i]-As[i-1]>0:
        tmp.append(1)
    elif As[i]-As[i-1]<0:
        tmp.append(-1)
    else:
        tmp.append(0)

seq = False
money = 1000
stock = 0
for i, pm in enumerate(tmp, 1):
    if pm==1:
        if seq == False:
            stock = As[i-1]
            seq = True
    if pm==-1:
        if stock:
            stock_num = money//stock
            money-=stock*stock_num

            max_ = As[i-1]
            money+=max_*stock_num

            seq = False
            stock = 0
    if len(tmp) == i:
        if stock<As[i] and stock!=0:
            stock_num = money//stock
            money-=stock*stock_num
            max_ = As[i]
            money+=max_*stock_num
print(money)

