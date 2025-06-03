def main():
    n = int(input())
    a = list(map(int,input().split()))
    f,s = {},{}
    for i in range(n):
        if i+1-a[i] not in f.keys():
            f[i+1-a[i]] = 1
        else:
            f[i+1-a[i]]+=1
        if i+1+a[i] not in s.keys():
            s[i+1+a[i]] = 1
        else:
            s[i+1+a[i]] += 1
    ans = 0
    for k in f.keys():
        if k in s.keys():
            ans += f[k] * s[k]
    print(ans)

if __name__ == "__main__":
    main()
