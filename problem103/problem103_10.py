def sell(rate, kabu):
    return rate * kabu
    
def buy(rate, money):
    kabu = money//rate
    otsuri = money % rate
    return kabu, otsuri
    
N,*A = map(int, open(0).read().split())
money = 1000
have_kabu = 0
for i in range(N):
    #売る
    money += sell(A[i], have_kabu)
    have_kabu = 0
    #買う    
    if i != N-1 and A[i] < A[i+1]: 
        have_kabu, money = buy(A[i], money)
print(money)