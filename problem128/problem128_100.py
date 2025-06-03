
X, N = map(int, input().split())
ps = list(map(int, input().split()))


for i in range(100):
    if X - i not in ps:
        print(X-i)
        exit()
    elif X + i not in ps:
        print(X+i)
        exit()
