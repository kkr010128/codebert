import copy
from sys import exit
n, k = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7

plus = []
minus = []
for a in A:
    if a >= 0:
        plus.append(a)
    else:
        minus.append(a)
plus.sort()
minus.sort(reverse=True)

def is_ans_plus():
    if len(plus) > 0:
        if n == k:
            if len(minus) % 2 == 0:
                return True
            else:
                return  False
        else:
            return True
    else:
        if k % 2 == 0:
            return True
        else:
            return False

ans = 1
if is_ans_plus():
    if k % 2 == 1:
        ans *= plus.pop()
        k -= 1
    for i in range(k // 2):
        plus_pair, minus_pair = -1, -1
        if len(plus) >= 2:
            plus_pair = plus[-1] * plus[-2]
        if len(minus) >= 2:
            minus_pair = minus[-1] * minus[-2]
        if plus_pair >= minus_pair:
            ans *= plus_pair
            plus.pop()
            plus.pop()
        else:
            ans *= minus_pair
            minus.pop()
            minus.pop()
        ans %= mod
else:
    ans = -1
    A = sorted([abs(a) for a in A])
    for i in range(k):
        ans *= A[i]
        ans %= mod
print(ans)
