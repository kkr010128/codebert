s = int(input())
MOD = 1000000007

kotae = [0 for _ in range(2001)]

kotae[0] = 0
kotae[1] = 0
kotae[2] = 0
kotae[3] = 1
kotae[4] = 1
kotae[5] = 1
kotae[6] = 2

for i in range(7,2001):
    kotae[i] = kotae[i-1] + kotae[i-3]
    kotae[i] = kotae[i] % MOD

print(kotae[s])