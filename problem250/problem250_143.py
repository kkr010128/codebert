def solve():
    from bisect import bisect_right, bisect, bisect_left
    x = int(input())
    n = 100100
    primes = set(range(2, n + 1))
    for i in range(2, int(n ** 0.5 + 1)):
        if i not in primes:
            i += 1
        else:
            ran = range(i * 2, n + 1, i)
            primes.difference_update(ran)
    primes = list(primes)
    y = bisect_left(primes, x)
    print(primes[y])
    
    
solve()
