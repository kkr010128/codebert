import math
 
X=int(input())
def ans165(X:int):
    cash=100#当初の預金額
    count=0
    while True:
        # cash=int(cash*1.01) #元本に１パーセントの利子をつけ小数点以下切り捨て # WA
        # cash = cash * 1.01 * 100 // 100 # 1%の利子をつけて100倍した後に100で割って整数部のみ取り出す # WA
        # cash += cash * 0.01 * 100 // 100 # 1%の利子を計算して100倍した後に100で割って整数部のみ取り出す # WA
        # cash += cash // 100 # 元本に100で割った整数部を足す # AC
        # cash += math.floor(cash * 0.01) # WA
        # cash += math.floor(cash / 100) # WA
        cash += math.floor(cash // 100) # WA
        count += 1#利子をつける回数だけcountを増やす
        if cash>=X:#cashがXの値以上になったらループ終了
            break
    return count
print(ans165(X))