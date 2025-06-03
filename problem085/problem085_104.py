import math
n = int(input())
a = list(map(int, input().split()))
nmax = 10**6

check = [0]*(nmax + 5)
for i in a:
    check[i] += 1

pairwise = True
for i in range(2, nmax + 5):
    cnt = 0
    for j in range(i, nmax + 5, i):
        cnt += check[j] 
    if cnt > 1:
        pairwise = False

if pairwise == True:
    print('pairwise coprime')
    exit()

x = 0
for i in a:
    x = math.gcd(x,i)
if x == 1:
    print('setwise coprime')
else:
    print('not coprime')



