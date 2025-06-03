from bisect import bisect_right

def eratosthenes(n):
    A = [i for i in range(2, n+1)]
    P = []
    i = 2
    while i**2 <= n:
        prime = min(A)
        P.append(prime)
        j = 0
        while j < len(A):
            if A[j] % prime == 0:
                A.pop(j)
                continue
            j += 1
        i += 1    
    for a in A:
        P.append(a)
    return P
    
x = int(input())
prime_table = eratosthenes(100003)
prime_set = set(prime_table)
if x in prime_set:
    print(x)
else:
    idx = bisect_right(prime_table, x)
    ans = prime_table[idx]
    print(ans)
