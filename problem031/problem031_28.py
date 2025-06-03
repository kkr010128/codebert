while True:
    n = int(input())
    if n == 0:
        break
    else:
        data_set = [int(i) for i in input().split()]
        m = sum(data_set) / n
        v = 0
        for i in data_set:
            diff = i - m
            v += diff ** 2
        v /= n
        print(v ** 0.5)