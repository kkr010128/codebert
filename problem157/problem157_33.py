def main():
    n = int(input())
    a = list(map(int,input().split()))
    sa,wa = {},{}
    for i in range(n):
        if a[i]+i+1 not in wa.keys():
            wa[a[i]+i+1]=1
        else:
            wa[a[i]+i+1]+=1
        if i-a[i] >0:
            if i+1-a[i] not in sa.keys():
                sa[i+1-a[i]]=1
            else:
                sa[i+1-a[i]]+=1
    ans = 0
    for k in sa.keys():
        if k in wa.keys():
            ans += sa[k]*wa[k]
    print(ans)


if __name__ == "__main__":
    main()
