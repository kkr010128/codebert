
N, K = list(map(int, input().split()))

MOD = 10**9+7


gcd_dict = {}
for i in range(K, 0, -1):

    number = pow((K//i), N, MOD)
    number %= MOD
    counter = 2
    while True:
        if counter*i in gcd_dict:
            number -= gcd_dict[counter*i]
            counter += 1
        else:
            gcd_dict[i] = number % MOD
            break

print(sum([i*j for i, j in gcd_dict.items()]) % MOD)