def main():
    N, A, B = map(int, input().split())
    ans = 0
    ans += (N // (A + B)) * A
    ans += min([N % (A + B), A])
    print(ans)


if __name__ == '__main__':
    main()
