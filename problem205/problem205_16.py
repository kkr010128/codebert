def main():
    n,p = map(int,input().split())
    s = input()

    if p == 2 or p == 5:
        ans = 0
        for i in range(n-1,-1,-1):
            if int(s[i]) % p == 0:
                ans += i+1
        print(ans)
        exit()

    l = [0]*p
    l[0] += 1
    s1 = s[::-1]
    ten = 1
    mod = 0
    for i in range(n):
        mod += int(s1[i])*ten%p
        mod %= p
        ten = ten*10%p
        l[mod] += 1
    ans = 0

    for i in l:
        ans += (i-1)*i//2
    print(ans)
if __name__ == "__main__":
    main()