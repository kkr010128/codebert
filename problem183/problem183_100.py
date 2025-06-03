N = int(input())

ans = []
for n in range(1, int(N ** 0.5) + 1):
    if (N - 1) % n == 0:
        ans.append(n)
        ans.append((N - 1) // n)

for k in range(2, int(N ** 0.5) + 1):
    if N % k != 0:
        continue

    x = N
    while x % k == 0:
        x //= k

    if x % k == 1:
        ans.append(k)

print(len(set(ans)))
