def main():
    S = input()
    T = input()

    cnt = 0
    for a, b in zip(S, T):
        cnt += a != b
    print(cnt)


if __name__ == '__main__':
    main()
