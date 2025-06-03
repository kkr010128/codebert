from bisect import bisect_left, bisect_right

n = int(input())
stick = list(map(int, input().split()))
stick.sort()

count = 0
for i in range(n):
    for j in range(i + 1, n):
        l = bisect_right(stick, stick[j] - stick[i])
        r = bisect_left(stick, stick[i] + stick[j]) # [l, r) が範囲
        if j + 1 >= r:
            continue
        count += r - max(l, j + 1)
print(count)