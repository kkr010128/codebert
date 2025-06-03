def main():
    a, b = map(int, input().split())
    maxv = int((101 / 0.1) - 1)
    for i in range(maxv+1):
        if (i*8//100 == a) and (i*10//100 == b):
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()
