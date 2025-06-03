def main():
    s = input()
    n = len(s) + 1
    ans = [-1] * (n)
    def right(i, ans):
        j = 1
        while True:
            ans[i + j] = max(ans[i + j], j)
            if i + j == n - 1:
                break
            if s[i + j] == '<':
                j += 1
            else:
                break
        return ans
    def left(i, ans):
        j = 1
        while True:
            ans[i - j] = max(ans[i - j], j)
            if i - j == 0:
                break
            if s[i - j - 1] == '>':
                j += 1
            else:
                break
        return ans
    for i in range(n):
        if i == 0:
            if s[i] == '<':
                ans[0] = 0
                ans = right(i, ans)
            else:
                pass
        elif i == n - 1:
            if s[i - 1] == '>':
                ans[n - 1] = 0
                ans = left(i, ans)
            else:
                pass
        else:
            if s[i] == '<' and s[i - 1] == '>':
                ans[i] = 0
                ans = right(i, ans)
                ans = left(i, ans)
            else:
                pass
    print(sum(ans))

if __name__ == '__main__':
    main()
