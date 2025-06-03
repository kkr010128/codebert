def main():
    n, m = map(int, input().split())
    num = [0] * n
    reserved = [False] * n
    for _ in range(m):
        s, c = map(int, input().split())
        s -= 1
        if reserved[s]:
            if c != num[s]:
                print(-1)
                exit()
        else:
            reserved[s] = True
            num[s] = c
    if n > 1 and not reserved[0]:
        num[0] = 1
    if n > 1 and num[0] == 0:
        print(-1)
    else:
        print("".join(map(str, num)))


if __name__ == "__main__":
    main()
