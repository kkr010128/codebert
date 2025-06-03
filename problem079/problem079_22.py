def main():
    import math
    s = int(input())
    mod = 10**9+7
    c = s//3
    ans = 0
    for i in range(1,c+1):
        l = s - i*3
        ans += (math.factorial(l+i-1)//math.factorial(l)//math.factorial(i-1)) % mod
    print(ans%mod)

if __name__ == "__main__":
    main()