import sys

n = int(input())
x = sorted(list(map(int, input().split())))

if len(list(set(x))) == 1:
    print(0)
    sys.exit()

if n == 1:
    print(0)
    sys.exit()

x_min = x[0]
x_max = x[n-1]
min_sum = 10000000
for p in range(x_min, x_max):

    sum = 0
    for e in x:
        len = (e - p)**2
        sum += len
    # print("p", p, "sum", sum, "min_sum", min_sum)
    if sum <= min_sum:
        min_sum = sum
print(min_sum)
