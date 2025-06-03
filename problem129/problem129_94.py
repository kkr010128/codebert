
N = int(input())
X = list(map(int, input().split()))

MAX = 10 ** 6 + 1
prime = [True] * MAX
counted = set()
for v in X:
    if v in counted:
        prime[v] = False
        continue
    for j in range(2 * v, MAX, v):
        prime[j] = False
    counted.add(v)

ans = 0
for v in X:
    ans += int(prime[v])
print(ans)
