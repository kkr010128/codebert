import sys
import math
N = int(input())
A = list(map(int, input().split()))

NUM = 10**6

gcd = A[0]
for i in range(1, N):
    gcd = math.gcd(gcd, A[i])
if gcd != 1:
    print("not coprime")
    sys.exit()


def osa_k(num):
    S = list(i for i in range(num+1))
    for i in range(2, int(num**0.5)+1):
        if S[i] < i:
            continue
        j = i**2
        while j <= num:
            if S[j] == j:
                S[j] = i
            j += i
    return S


prime = osa_k(NUM)
S = [False]*(NUM+1)
for num in A:
    tmp = prime[num]
    while num > 1:
        num //= tmp
        if tmp == prime[num]:
            # S[tmp] = True
            continue
        if S[tmp]:
            print("setwise coprime")
            sys.exit()
        S[tmp] = True
        tmp = prime[num]
print("pairwise coprime")


        

