import sys

def solve():
    a, b = map(int, input().split())
    ans = gcd(a, b)
    print(ans)

def gcd(a, b):
    return gcd(b, a % b) if b else a

if __name__ == '__main__':
    solve()