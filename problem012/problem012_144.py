import sys

def solve():
    n = int(sys.stdin.readline())
    ans = 0

    for i in range(n):
        num = int(sys.stdin.readline())

        ans += is_prime(num)

    print(ans)

def is_prime(n):
    if n < 2:
        return False

    for p in range(2, n + 1):
        if p*p > n:
            break
        if n % p == 0:
            return False

    return True

if __name__ == '__main__':
    solve()