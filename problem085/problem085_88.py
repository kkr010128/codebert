from math import gcd
from functools import reduce
from sys import exit

# O(A+N)解
MAX_A = 1000000
lowerst_prime = [0] * (MAX_A + 1) # 最小の素因数をいれる(2以上をみていけばいい)
primes = [] # MAX_A以下の素数の集合
count = [0] * (MAX_A + 1) # 約数として出てくる回数を数える
for i in range(2, MAX_A + 1): # 線形時間で処理してくれる
    if lowerst_prime[i] == 0:
        lowerst_prime[i] = i
        primes.append(i)
    for p in primes:
        if p > lowerst_prime[i] or i * p > MAX_A:
            break
        lowerst_prime[i * p] = p # p が i * p のもっとも小さな素因数となるときのみ更新されるので、線形時間アルゴリズムとなる
# 入力
N = int(input())
A = [*map(int, input().split())]
if reduce(gcd, A) != 1:
    print("not coprime")
    exit(0)
for i in range(N):
    while A[i] > 1:
        divide = lowerst_prime[A[i]]
        if count[divide]:
            # A[x] % i == A[y] % i == 0 となるx != yが存在するので、i | gcd(x, y) となる
            print("setwise coprime")
            exit(0)
        count[divide] += 1
        while A[i] % divide == 0: # 割れるだけ割る
            A[i] //= divide
print("pairwise coprime")