"""
Nが1になるようなKは、
・K^x = NになるようなKか
・K^x(K*y+1) = N になるようなKである。
後者は前者を包括するので、後者についてのみカウントすればよい。
Kの数を求めるために、後者をさらに2種類に分ける
・x > 0の場合
・x == 0の場合
前者の場合、KはNの約数なので、Nの約数全部に関して条件を満たすか調べればよい。Nの約数はそんなに多くならないので、時間はかからない。
後者の場合だと、KはN-1の約数の数だけ存在するのでN-1の約数の数を求めればよい。
"""
from collections import Counter

def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

N = int(input())
ans = 0
#x>0の場合を調べる
#Nを素因数分解する
devisers = []
d = 2
while d*d < N:
    if N % d == 0:
        devisers.append(d)
        devisers.append(N//d)
    d += 1
if d*d == N:
    devisers.append(d)

for d in devisers:
    dummyN = N
    while dummyN % d == 0:
        dummyN //= d
    if dummyN%d == 1:
        ans += 1


#x == 0 になるようなKの数を調べる。
#N-1を素因数分解する。
tmp = []
dummyN = N-1
ceil = int(dummyN**0.5)
for d in range(2,ceil+1):
    while dummyN % d == 0:
        tmp.append(d)
        dummyN //= d
if dummyN != 1:
    tmp.append(dummyN)
    dummyN //= dummyN

divideN = Counter(tmp)
commonDCnt = 1
for v in divideN.values():
    commonDCnt *= (v+1)
ans += commonDCnt

print(ans)
