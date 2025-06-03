import math
N = int(input())
S = input()

lst0 = [0]*N
lst1 = [0]*N
lst0[0] = 1
lst1[0] = 1
c = S.count('1')
m0 = int(S[-1])
m1 = int(S[-1])
for i in range(1, N):
    lst0[i] += (lst0[i-1]*2)%(c+1)
    if c == 1:lst1[i] = 0
    else: lst1[i] += (lst1[i-1]*2)%(c-1)
    m0 += lst0[i] * int(S[N - 1- i])
    m0 %= c+1
    m1 += (lst1[i] * int(S[N - 1 - i]))
    if c == 1: m1 = 0
    else: m1 %= c-1

memo = [0]*(N+1)

def calc(a):
    global ans, memo
    if a == 0: return ans
    ans += 1
    if memo[a] != 0:
        b = memo[a]
    else:
        b = bin(a).count('1')
        memo[a] = b
    return calc(a%b)
    
for i in range(N):
    if S[i] == '1':
        b = c - 1
        if b == 0: a = 0
        else: a = max((m1 - lst1[N - 1 - i])%b, (m1 - lst1[N - 1 - i]+ b)%b)
    else:
        b = c + 1
        a = (m0 + lst0[N - 1 - i])%b
    if b == 0: print(0)
    elif a == 0:print(1)
    else:
        ans = 1
        print(calc(a))