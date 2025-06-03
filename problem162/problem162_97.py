from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def main():
    n, m = map(int, input().split())
    a = 1
    d = n - 1
    for _ in range(m):
        if d % 2 == 1 and (d == n // 2 or d == n // 2 - 1):
            d -= 1
        print(a, a + d)
        a += 1
        d -= 2

main()