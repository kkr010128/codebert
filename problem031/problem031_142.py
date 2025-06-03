while True:
    n = int(input())
    if n == 0:
        break
    data = input().split()
    import math
    sum = 0
    for i in range(n):
        sum = sum + int(data[i])
    average = sum / n
    a = 0
    for i in range(n):
        a = a + (int(data[i]) - average)**2
    print('{}'.format(math.sqrt(a/n)))
