def main():
    K = int(input())
    v = 7 % K
    for i in range(K+5):
        if v == 0:
            print(i+1)
            return
        v = v * 10 + 7
        v %= K
    print(-1)


if __name__ == '__main__':
    main()
