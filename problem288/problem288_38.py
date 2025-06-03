def make_divisors(n):
    '''
    nの約数の配列を返す
    '''
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def solve():
    N = int(input())
    D = make_divisors(N)
    ans = N - 1
    for d in D:
        ans = min(ans, N // d - 1 + d - 1)
    print(ans)

if __name__ == "__main__":
    solve()
