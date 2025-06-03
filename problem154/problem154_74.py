N, K = list(map(int, input().split(' ')))

table = {l for l in range(1, N + 1)}
have = set()

for i in range(K):
    d = int(input())
    nums = list(map(int, input().split(' ')))
    have = have | set(nums)

ans = len(table - have)

print(ans)