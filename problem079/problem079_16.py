S = int(input())
DP = [0] * (S + 1)
Mod = 10 ** 9 + 7

if S >= 3:
    DP[0] = 1
    DP[1] = 0
    DP[2] = 0
    for TS in range(3,S+1):
        DP[TS] = DP[TS-1] + DP[TS-3]
    print(DP[S] % Mod)
else:
    print(0)