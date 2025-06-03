X,N = map(int, input().split())
P = list(map(int, input().split()))

min = 51

for i in range(102):
    if i not in P and abs(X-i) < min:
        min = abs(X-i)
        ans = i

print(ans)