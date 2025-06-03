def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p_tuple = tuple(map(int, input().split()))

    radius = 0
    for i in range(100):
        if x-radius not in p_tuple:
            print(x-radius)
            return
        elif x+radius not in p_tuple:
            print(x+radius)
            return
        else:
            radius += 1


if __name__ == '__main__':
    main()
