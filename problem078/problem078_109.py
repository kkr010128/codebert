# --------- C -----------
MOD = 10**9 + 7
N = int(input())

answer = (10**N - 9**N) + (10**N - 9**N) - (10**N - 8**N)

print(answer % MOD)