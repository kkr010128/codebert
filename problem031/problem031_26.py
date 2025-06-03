import math

while True:
    x = int(input())
    # x = 5
    if x==0:
        break
    data = list(map(float, input().split()))
    # data = list(map(float, '70 80 100 90 20'.split()))
    average = sum(data)/x
    temp = 0
    for d in data:
        temp += math.pow(d - average, 2)
        # print(math.pow(d - average, 2))
    stdev = math.sqrt(temp / x)
    print(stdev)
