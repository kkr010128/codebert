import math
while True:
    count = int(input())
    if count == 0:
        break

    data = [int(i) for i in input().split()]
    m = sum(data) / len(data)
    a = sum([(x - m) ** 2 for x in data]) / count

    print('{0:.5f}'.format(math.sqrt(a)))