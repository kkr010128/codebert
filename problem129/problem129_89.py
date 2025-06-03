import heapq

n = int(input())
a = list(map(int, input().split()))
dp = [0] * (pow(10, 6) + 5)
heapq.heapify(a)
heapq.heappush(a, 1000003)
ans = -1
y = 0
for _ in range(n + 1):
    x = heapq.heappop(a)
    if x == y and dp[x] == 2:
        dp[x] = 1
        ans -= 1
        continue
    elif dp[x] == 0:
        ans += 1
        dp[x] = 2
        i = 2
        while i * x <= 1000000:
            dp[i * x] = 1
            i += 1
    y = x
print(ans)