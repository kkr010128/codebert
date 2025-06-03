def main():

    data_count = int(input())
    data = [list(map(int, input().split())) for i in range(data_count)]

    for item in data:
        item.sort()
        print('YES') if item[0]**2 + item[1]**2 == item[2]**2 else print('NO')


main()