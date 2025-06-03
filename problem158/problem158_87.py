def main():
    base_distance = int(input().rstrip())
    min_distance, max_distance = (int(i) for i in input().rstrip().split(' '))
    if (max_distance // base_distance) * base_distance >= min_distance:
        print('OK')
    else:
        print('NG')


if __name__ == '__main__':
    main()
