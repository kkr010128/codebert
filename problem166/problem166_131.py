from collections import defaultdict
MOD = 2019
def main():
    S = input()
    dp = [0] * (len(S)+1)
    ex = 1
    for i in range(len(S)):
        dp[i+1] = (int(S[-1-i])*ex + dp[i]) % MOD
        ex *= 10
        ex %= MOD
    d = defaultdict(int)
    for i in range(len(S)+1):
        d[dp[i]] += 1
    output = 0
    for i in d.keys():
        output += (d[i] * (d[i]-1) // 2)
    print(output)
    return

if __name__ == '__main__':
    main()
