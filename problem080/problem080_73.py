import sys
input = sys.stdin.readline
INF = 10**18
sys.setrecursionlimit(10**6)

def li():
    return [int(x) for x in input().split()]


N = int(input())

xs, ys = [], []
for i in range(N):
    x, y = li()
    xs.append(x)
    ys.append(y)


def get_max_manhattan_distanse(xs, ys):
    X = [xs[i] + ys[i] for i in range(len(xs))]
    Y = [xs[i] - ys[i] for i in range(len(xs))]
    # return max(max(X) - min(X), max(Y) - min(Y))
    X.sort()
    Y.sort()
    return max(X[-1] - X[0], Y[-1] - Y[0])

ans = get_max_manhattan_distanse(xs, ys)
print(ans)