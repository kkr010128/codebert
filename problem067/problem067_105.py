turn = int(input())

point_taro = point_hanako = 0

for i in range(turn):
    taro,hanako = input().split()

    if taro > hanako:
        point_taro += 3
    elif hanako > taro:
        point_hanako += 3
    else:
        point_taro += 1
        point_hanako += 1

print("{} {}".format(point_taro,point_hanako))
