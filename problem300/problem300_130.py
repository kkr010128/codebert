import numpy as np

def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    table = sorted(table)
    return table

def make_prime(U):
    is_prime = np.zeros(U,np.bool)
    is_prime[2] = 1
    is_prime[3::2] = 1
    M = int(U**.5)+1
    for p in range(3,M,2):
        if is_prime[p]:
            is_prime[p*p::p+p] = 0
    return is_prime, is_prime.nonzero()[0]
A, B = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

A_list = set(divisor(A))
B_list = set(divisor(B))

list = A_list & B_list

#_, primes = make_prime(10**8)

cnt = 1

for i in list:
    if is_prime(i):
        cnt += 1

print(cnt)