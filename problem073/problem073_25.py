def main():
    n = int(input())
    cnt = 0
    # aが1からn-1まで動くと考える
    for a in range(1, n):
        # a*bがn-1以下であると考える
        cnt += (n-1) // a
    print(cnt)

if __name__ == '__main__':
    main()