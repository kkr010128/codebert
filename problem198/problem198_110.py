def main():
    from string import ascii_lowercase
    dic = {i: s for i, s in enumerate(ascii_lowercase)}
    N = int(input())
    ans = []

    def dfs(s, mx):
        if len(s) == N:
            print(s)
            return
        else:
            for i in range(mx+2):
                v = s + dic[i]
                mx = max(mx, i)
                dfs(v, mx)
    dfs("a", 0)


if __name__ == '__main__':
    main()
