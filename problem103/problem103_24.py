def sell(rate,kabu):
    money = rate * kabu
    return money
    
def buy(rate,money):
    kabu = money//rate
    otsuri = money % rate
    return kabu,otsuri
    
N,*A = map(int,open(0).read().split())
max_money = 1000
have_money = 1000
have_kabu = 0
for i in range(N-1):
    if A[i] < A[i+1] and have_money > A[i]: #買う
        have_kabu,have_money = buy(A[i],have_money)
    if A[i] > A[i+1]: #売る
        have_money += sell(A[i],have_kabu)
        have_kabu = 0
        max_money = max(max_money,have_money)
have_money += sell(A[-1],have_kabu)    
max_money = max(max_money,have_money)
print(max_money)        