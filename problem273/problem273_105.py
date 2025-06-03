import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = LI()
A = LI()

for i in range(N):
    A[i] -= 1

B = [0]  # Aの累積和をKで割ったもの
for i in range(N):
    B.append((B[-1]+A[i]) % K)

from collections import defaultdict

# 要素の個数がKを超えないことに注意

if N < K:
    d = defaultdict(int)
    for n in B:
        d[n] += 1
    ans = 0
    for n in d.keys():
        m = d[n]
        ans += m*(m-1)//2
    print(ans)
else:
    d = defaultdict(int)
    ans = 0
    for i in range(N):  # A[i]から始まる部分列を考える
        if i == 0:
            for j in range(K):
                d[B[j]] += 1
            ans += d[B[i]]-1
        elif i <= N-K+1:
            d[B[K+i-1]] += 1
            d[B[i-1]] -= 1
            ans += d[B[i]]-1
        else:
            d[B[i-1]] -= 1
            ans += d[B[i]]-1
    print(ans)

