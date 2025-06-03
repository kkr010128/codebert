from collections import Counter
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
A_lst = list(map(int,input().split()))
S = Counter(A_lst)
sums = 0
#for i in S.keys():
#    if S[i] > 1:
#        sums += combinations_count(S[i], 2)

for c, i in S.items():
    sums += i*(i-1)//2

for j in range(1, N + 1):
    if S[A_lst[j-1]] == 2:
        print(sums - 1)
    elif S[A_lst[j-1]] > 2:
        print(int(sums - S[A_lst[j-1]] * (S[A_lst[j-1]]-1) * 0.5 + (S[A_lst[j-1]] - 1) * (S[A_lst[j-1]] - 2) * 0.5))
    else:
        print(sums)