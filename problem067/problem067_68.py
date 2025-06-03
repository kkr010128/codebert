count = int(input())
point = {'taro': 0, 'hanako': 0}
for i in range(count):
    (taro, hanako) = [s for s in input().split()]
    if (taro > hanako) - (taro < hanako) == 0:
        point['taro'] += 1
        point['hanako'] += 1
    elif (taro > hanako) - (taro < hanako) > 0:
        point['taro'] += 3
    else:
        point['hanako'] += 3

print(point['taro'], point['hanako'])