def main():
    d = int(input())
    c = list(map(int,input().split()))
    s = [list(map(int,input().split())) for _ in range(d)]
    t = [int(input()) for _ in range(d)]
    
    ptn = len(c)
    last = [0]*ptn
    res = 0

    for i in range(d):
        sel = t[i] - 1
        last[sel] = i+1

        mns = 0
        for j in range(ptn):
            mns += c[j] * (i+1 - last[j])

        res += s[i][sel] - mns
        print(res)


if __name__ == '__main__':
    main()
