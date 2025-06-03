n = int(input())
mod = 10**9+7
num = 10**n%mod - 2*(9**n%mod)%mod + 8**n%mod
print(num if num>=0 else num+mod)
