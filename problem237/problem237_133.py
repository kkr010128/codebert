n = int(input())

intervals = []

for _ in range(n):
    x, l = list(map(int, input().split()))
    intervals.append((x-l, x+l))

intervals = sorted(intervals, key=lambda x: x[1])

cnt = n
lastEnd = intervals[0][1]

for i in range(1, n):
    if intervals[i][0] < lastEnd:
        cnt -= 1
    else:
        lastEnd = intervals[i][1]

print(cnt)