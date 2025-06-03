import math

def sieve_of_erastosthenes(num):
    is_prime = [True for i in range(num+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(num**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, num + 1, i):
            is_prime[j] = False
    return [i for i in range(num + 1) if is_prime[i]]

N = int(input())
A = [int(i) for i in input().split()]
ans = math.gcd(A[0], A[1])
tmp = math.gcd(A[0], A[1])
for i in range(2, N):
    ans = math.gcd(ans, A[i])
if ans > 1:
    print('not coprime')
    exit()
maxA = max(A)
l = sieve_of_erastosthenes(maxA)
B = [False for i in range(maxA+1)]
for i in range(N):
    B[A[i]] = True
flag = False
for each in l:
    tmp = each
    counter = 0
    while True:

        if B[tmp]:
            counter += 1
        tmp += each
        if tmp > maxA:
            break
    if counter > 1:
        flag = True
        break


if flag:
    print('setwise coprime')
else:
    print('pairwise coprime')