
N = int(input())
X = list(map(int, input().split()))

ans = [0] * (N + 1)
for v in X:
    ans[v] += 1

print(*ans[1:], sep="\n")
