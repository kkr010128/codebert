k, n = map(int, input().split())
a = [int(i) for i in input().split()]
a += [a[0] + k]
sum = 0
max = 0

# 最も長い辺を求める
for i in range(n):
    d = abs(a[i] - a[i + 1])
    sum += d
    if max < d:
        max = d
# 最も長い辺を通らずに1周回るのが最小
print(sum - max)