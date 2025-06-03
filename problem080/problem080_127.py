n = int(input())

xy_sum = []
xy_dif = []
for i in range(n) :
    x, y = map(int, input().split())
    xy_sum.append(x + y)
    xy_dif.append(x - y)

print(max(abs(max(xy_sum) - min(xy_sum)), abs(max(xy_dif) - min(xy_dif))))