from fractions import gcd

# gcd(A,B)の素因数分解したときの素数の数+1が最大
# なぜならば任意の公約数C|A,C|BはC|gcd(A,B)
# Cとして素因数+1より大きいの数を選ぶと、Cはどこかの素数で重複して互いに素にならない

A,B = map(int, input().split())
D = gcd(A,B)

ret = 1
prime_len = 10**6+1
prime_factor = [False]*prime_len
for p in range(2, prime_len):
    while D%p == 0:
        if prime_factor[p] == False:
            ret += 1
            prime_factor[p] = True
            
        D = D//p
        
    if D == 1: break

# 10^6以下の素因数を探索して、1でなければ10^12以下の数は素数である。（10^6<p,p^\primeならば10^12 < p \cdot p^\prime）
if D != 1: ret += 1
    
print(ret)