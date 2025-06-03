import sys

def lcm(a, b):
    a, b = max(a, b), min(a, b)
    c = a * b
    while a % b > 0:
        a, b = b, a % b
    return c // b


def solve():
    input = sys.stdin.readline
    X = int(input())
    L = lcm(360, X)
    print(L // X)

    return 0

if __name__ == "__main__":
    solve()