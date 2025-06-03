N, K = map(int, input().split())

# all selected
upper = sum(range(N+1))
lower = sum(range(N+1))
answer = 1

for k in range(N, K - 1, -1):
    upper -= N - k
    lower -= max(0, k)
    answer += upper - lower + 1
    # print(k, upper, lower, answer)
print(answer % (10 ** 9 + 7))