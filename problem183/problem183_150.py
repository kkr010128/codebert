def divisors(n):
    i = 1
    table = set()
    while i * i <= n:
        if not n % i:
            table.add(i)
            table.add(n//i)
        i += 1
    table = list(table)
    return table
N = int(input())
k = 2
res = 0
while k*k<=N:
    n = N
    while not n%k:
        n//=k
    if (n%k==1 or n==1) and n!=N:
        res += 1
    k += 1
a = divisors(N-1)
print(len(a)+res)