def main():
    n = int(input())
    a = sorted(map(int,input().split()))
    fld = [-1 for i in range(a[-1]+1)]
    flg = []
    for i in range(n):
        if fld[a[i]]==-1:
            fld[a[i]]=1
            for j in range(2,a[-1]//a[i]+1):
                fld[a[i]*j] = 0
        elif fld[a[i]]==1:
            flg.append(a[i])
    for i in range(len(flg)):
        fld[flg[i]] = 0
    ans = 0
    for i in range(len(fld)):
        if fld[i] == 1:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
