def main():
    from string import ascii_lowercase

    N = int(input())

    ans = []

    def dfs(s='a', ma='a'):
        if len(s) == N:
            ans.append(s)
            return

        for c in ascii_lowercase:
            dfs(s + c, max(c, ma))
            if c > ma: break

    dfs()

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
