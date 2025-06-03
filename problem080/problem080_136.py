
def resolve():
    N = int(input())
    Z = []
    W = []

    for i in range(N):
        x, y = map(int, input().split())
        Z.append(x + y)
        W.append(x - y)

    a = max(Z) - min(Z)
    b = max(W) - min(W)
    print(max(a, b))


if __name__ == "__main__":
    resolve()