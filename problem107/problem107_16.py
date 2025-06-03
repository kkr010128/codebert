import sys
sys.setrecursionlimit(10000000)
N = int(input())
X = input()
zero_pop = X.count('1') + 1
one_pop = X.count('1') - 1
one_mod, zero_mod = 0, 0

for b in X:
    if one_pop != 0:
        one_mod = (one_mod * 2 + int(b)) % one_pop
    zero_mod = (zero_mod * 2 + int(b)) % zero_pop

pop = {0:0}
def popcount(n):
    if n in pop:
        return pop[n]
    pop[n] = popcount(n // 2) + n % 2
    return pop[n]
memo = {0:0}
def f_count(n):
    if n in memo:
        return memo[n]
    memo[n] = f_count(n % popcount(n)) + 1
    return memo[n]
one_p = {0:1}
def one_pow(n):
    if n in one_p:
        return one_p[n]
    one_p[n] = one_pow(n - 1) * 2 % one_pop
    return one_p[n]
zero_p = {0:1}
def zero_pow(n):
    if n in zero_p:
        return zero_p[n]
    zero_p[n] = zero_pow(n - 1) * 2 % zero_pop
    return zero_p[n]
for i in range(N):
    if X[i] == '1' and one_pop == 0:
        print(0)
        continue
    if X[i] == '1':
        x = one_mod
        x -= one_pow(N-1-i)
        x %= one_pop
    elif X[i] == '0':
        x = zero_mod
        x += zero_pow(N-1-i)
        x %= zero_pop
    
    print(f_count(x) + 1)