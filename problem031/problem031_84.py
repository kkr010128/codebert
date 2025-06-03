import statistics as stats

while True:
    n = int(input())
    if n == 0:
        break
    data = list(map(int, input().split()))
    SD = stats.pstdev(data)
    print("{:.5f}".format(SD))