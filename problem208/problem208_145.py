def main():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    ans = list()
    for i in range(n):
        ans.append(0)
    for i in range(m):
        if n != 1 and s[i] == 1 and c[i] == 0:
            print(-1)
            exit()
        if ans[s[i]-1] == 0 or ans[s[i]-1] == c[i]:
            ans[s[i]-1] = c[i]
        elif ans[s[i]-1] != 0 and ans[s[i]-1] != c[i]:
            print(-1)
            exit()
    if n != 1:
        if ans[0] == 0:
            ans[0] = 1
        print(*ans, sep='')
    else:
        print(*ans, sep='')

if __name__ == '__main__':
    main()