n, k = map(int, input().split())
a = list(map(int, input().split()))

for count in range(k):
    range_diff = [0] * n
    for pos in range(n):
        candidate_min = pos - a[pos]
        candidate_max = pos + a[pos] + 1
        if pos - a[pos] >= 0:
            min = pos - a[pos]
        else:
            min = 0
        range_diff[min] += 1
        if candidate_max <= n-1:
            range_diff[candidate_max] -= 1
    for i in range(1, n):
        range_diff[i] += range_diff[i-1]
    a = range_diff
    if count >= 43:
        break

print(' '.join(list(map(str,a))))