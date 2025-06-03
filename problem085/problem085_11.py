import sys, math
input = sys.stdin.readline
n = int(input())
a = [int(x) for x in input().split()]

m = max(a)
primes = list(range(m+1))
primes[1] = 0
for i in range(2, m+1, 2): primes[i] = 2

for i in range(3, int(m ** 0.5)+1):
    if primes[i] < i: continue
    for j in range(i, m+1, i):
        primes[j] = i

b = [0] * (m + 1)
jdg_p = True
for aa in a:
    aset = set()
    while aa != 1:
        aset.add(primes[aa])
        aa //= primes[aa]
    for aaset in aset:
        b[aaset] += 1
        if b[aaset] >= 2:
            jdg_p = False
            break
        else:
            b[aaset] += 1
    if not jdg_p: break

x = a[0]
jdg_s = True
for aa in a[1:]:
    x = math.gcd(x, aa)
if x != 1: 
    jdg_s = False

if jdg_p: print('pairwise coprime')
elif jdg_s: print('setwise coprime')
else: print('not coprime')