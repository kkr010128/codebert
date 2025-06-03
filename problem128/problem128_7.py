X, N = map(int, input().split())
P = list(map(int, input().split()))
st = set(P)
for i in range(111):
    if not X - i in st:
        print(X - i)
        exit(0)
    if not X + i in st:
        print(X + i)
        exit(0)
