def main():
    n, p = map(int, input().split())
    s = input()
    mu = [None]*n
    ans = 0
    c = [0]*p
    if 10%p == 0:
        ss = map(int, s)
        ss = list(ss)
        for i in range(n):
            if ss[i]%p == 0:
                ans += i+1
        print(ans)
        return
    sr = s[::-1]
    ssr = map(int, sr)
    tens = 1
    v = 0
    for i, si in enumerate(ssr):
        v = (v + (si%p)*tens)%p
        mu[i] = v
        c[v] += 1
        tens *= 10
        tens %= p
    c[0] += 1
    for i in c:
        if i:
            ans += ((i-1)*i)//2
        
    print(ans)
    

if __name__ == "__main__":
    main()