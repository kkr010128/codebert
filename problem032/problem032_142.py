n, x, y = int(input()), list(map(int, input().split())), list(map(int, input().split()))


def dist(p):
    return pow(sum(pow(abs(a - b), p) for a, b in zip(x, y)), 1.0 / p)


for i in [1, 2, 3]:
    print(dist(i))

print(max(abs(a - b) for a, b in zip(x, y)))