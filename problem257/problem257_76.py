def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a_s = set(a)
    cnt = 0
    order = 1
    if not 1 in a_s:
        print(-1)
        exit()
    else:
        for i in range(len(a)):
            if a[i] != order:
                cnt += 1
            if a[i] == order:
                order += 1
    print(cnt)

if __name__ == '__main__':
    main()
