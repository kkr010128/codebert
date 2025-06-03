mod_val = 10**9+7
n, k = map(int, input().split())
factorials = [1]*(n+1)  # values 0 to n
for i in range(2, n+1):
  factorials[i] = (factorials[i-1]*i)%mod_val
def mod_binomial(a, b):
  numerator = factorials[a]
  denominator = (factorials[b]*factorials[a-b])%mod_val
  invert = pow(denominator, mod_val-2, mod_val)
  return (numerator*invert)%mod_val
partial = 0
# m is number of rooms with no people
for m in range(min(k+1, n)):
  # m places within n to place the 'no people' rooms
  # put n-(n-m) people in n-m rooms (n-m) must be placed to be non-empty
  partial = (partial + (mod_binomial(n, m) * mod_binomial(n-1, m))%mod_val)%mod_val
print(partial)