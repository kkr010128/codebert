def make_divisors(n):
    ans = 10 ** 12 + 10
    i = 1
    while i*i <= n:
        if n % i == 0:
            t = 0
            if i != n // i:
                t = i + (n//i) - 2
            else:
                t = i * 2 - 2
            #print(i, n//i, t)
            if ans > t:
                ans = t
        i += 1
    return ans

n = int(input())
print(make_divisors(n))