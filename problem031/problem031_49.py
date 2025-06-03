while True:
    num = int(input())
    if num == 0:
        break
    data = list(map(int, input().split()))
    datasqr = [i ** 2 for i in data]
    print("%lf" % (sum(datasqr) / num - (sum(data) / num) ** 2) ** 0.5)
