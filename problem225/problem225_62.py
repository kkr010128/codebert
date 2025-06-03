def main():
    H, A = map(int, input().split())
    ans = (H + (A - 1)) // A
    print(ans)


if __name__ == '__main__':
    main()
