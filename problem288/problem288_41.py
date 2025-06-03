def resolve():
    n = int(input())
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        divisors.sort()
        return divisors

    divisors = make_divisors(n)
    min_pair = 10**19
    for i in divisors:
        pair_i = n//i
        min_pair = min(min_pair, ((i-1)+(pair_i-1)))
    print(min_pair)
resolve()