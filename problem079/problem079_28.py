def main():
    s = int(input())
    if s < 3:
        print(0)
    else:
        total = [0]*(s+1)
        total[3] = 1
        mod = 10**9+7
        for i in range(4, s+1):
            total[i] = (total[i-3] + 1) + total[i-1]
            total[i] %= mod
        print((total[s-3]+1)%mod)

if __name__ == "__main__":
    main()