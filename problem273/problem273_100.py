from collections import defaultdict


n, k = map(int, input().split())
A = list(map(int, input().split()))
delta_count = defaultdict(int)
cumA = [0]
total = 0
for a in A:
    total += a
    total %= k
    cumA.append(total)

for i in range(1, min(n+1, k)):
    num = cumA[i]
    delta = (num - i) % k
    delta_count[delta] += 1

ans = delta_count[0]
left = 1
right = min(k-1, n)

while left <= n-1:
    popleft = (cumA[left] - left) % k
    delta_count[popleft] -= 1
    if right <= n-1:
        right += 1
        num = cumA[right]
        append = (num - right) % k
        delta_count[append] += 1

    desire = (cumA[left] - left) % k
    ans += delta_count[desire]
    left += 1

print(ans)