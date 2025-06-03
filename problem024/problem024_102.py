def check_p(packages, n, trucks, max_p):
    i = 0
    for _ in range(trucks):
        sum = 0
        while sum + packages[i] <= max_p:
            sum += packages[i]
            i += 1
            if i == n:
                return i
    return i

n, k = map(int, input().split())
packages = []
for _ in range(n):
    packages.append(int(input()))

left = 0
right = 10 ** 5 * 10 ** 4
while left + 1 < right:
    mid = (left + right) // 2
    num = check_p(packages, n, k, mid)
    if num < n:
        left = mid
    else:
        right = mid
print(right)

