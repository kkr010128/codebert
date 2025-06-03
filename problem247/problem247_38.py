import fractions, sys
input = sys.stdin.buffer.readline


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


def calc(n, m):
    for i in range(cycle//m+1):
        X = m * (i + 0.5)
        if X > M:
            print(0)
            exit()
            return
        flag = True
        for x in n:
            if (X - x // 2) % x != 0:
                flag = False
                break
        if flag:
            return int(X)
    print(0)
    exit()
    return


N, M = map(int, input().split())
A = list(map(int, input().split()))
cycle = 1
ma = 0
for a in A:
    cycle = lcm(cycle, a)
    ma = max(ma, a)
start = calc(A, ma)

print((M - start) // cycle + 1)

