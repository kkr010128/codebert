def main():
    N = input()
    S, T = input().split()
    ans = ""
    for s, t in zip(S, T):
        ans += s + t
    print(ans)


if __name__ == '__main__':
    main()
