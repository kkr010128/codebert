def find_divisors(n):
    divisors = set()
    
    div = 1
    while div ** 2 <= n:
        if n % div == 0:
            divisors.add(div)
            divisors.add(n // div)
        div += 1
    
    return divisors


def main():
    n = int(input())
    
    res = 0
    
    for k in find_divisors(n) - {1}:
        t = n
        while t % k == 0:
            t //= k
        if t % k == 1:
            res += 1
    
    res += len(find_divisors(n - 1)) - 1
    
    print(res)


main()
