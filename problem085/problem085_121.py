from functools import lru_cache
import math

def main():
    n=int(input())
    a=list(map(int,input().split()))
    x=set()
    y=a[0]
    pair=True
    for i in a:
        if pair:
            p=set(prime_factorize(i))
            if len(x&p)>0:
                pair=False
            x|=p
        y=math.gcd(y, i)
    if pair:
        print("pairwise coprime")
    elif y==1:
        print("setwise coprime")
    else:
        print("not coprime")

# 素数リスト（エラトステネスの篩）
@lru_cache(maxsize=None)
def primes(n:int) -> list:
    '''n以下の全素数をlistで返す'''
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

# 素数判定（単純な素数判定なら十分早い。大量にやる場合はX in primesがよさそう）
@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    '''引数nが素数であればTrue、そうでなければFalseを返す'''
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# 素因数分解
def prime_factorize(n: int) -> list:
    '''引数nの素因数分解結果のlistを返す。'''
    arr = []
    # 2で割り続け奇数まで還元する
    while n % 2 == 0:
        arr.append(2)
        n //= 2
    # sqrt(n)までの素数で試し割
    for f in primes(int(n**0.5)):
        while n % f == 0:
            arr.append(f)
            n //= f
    if n != 1:
        arr.append(n)
    return arr

if __name__ == "__main__":
    main()