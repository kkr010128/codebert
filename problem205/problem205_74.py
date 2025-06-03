def main():
    n, mod = map(int, input().split())
    s = input().rstrip()
    a = [int(c)%mod for c in s]
    ans = 0
    if mod == 2 or mod == 5:
        for i in range(n):
            if a[i] == 0:
                ans += i + 1
    else:
        mul = 10 % mod
        for i in reversed(range(n-1)):
            a[i] = (a[i]*mul + a[i+1]) % mod
            mul = mul*10 % mod
        b = [0] * mod
        b[0] = 1
        for i in reversed(range(n)):
            ans += b[a[i]]
            b[a[i]] += 1
    print(ans)

if __name__ == "__main__":
    main()