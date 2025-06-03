X,N = map(int, input().split())
if N == 0:
    print(X)
    exit()
P = list(map(int, input().split()))
P.sort(reverse=True)

for i in range(105):
    if X - i not in P:
        print(X - i)
        break
    if X + i not in P:
        print(X + i)
        break