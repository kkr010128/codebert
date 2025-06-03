import math

while True:
    n = int(input())
    if n == 0:
        break

    arr = list(map(int, input().split()))
    m = sum(arr) / n
    t = 0
    for i in range(n):
        t += math.pow(arr[i] - m, 2)
    a = math.sqrt(t/n)
    print("{0:5f}".format(a))

