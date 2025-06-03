X, N = map(int, input().split())
if N == 0:
    print(X)
    exit()
p = list(map(int, input().split()))
ans = -1

for i in range(0,102):
    if i not in p:
        if abs(i-X) < abs(ans-X):
            ans = i
print(ans)