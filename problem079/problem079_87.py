mod = 1000000007
ans = 0
power = [0 for i in range(2005)]
power[0] = 1

for i in range(1,2001):
    power[i] = power[i-1] * i

def C(x,y):
    return 0 if x < y else power[x] // power[y] // power[x-y]

def H(x,y):
    return C(x+y-1,y-1)

n = int(input())
for i in range(3,n+1,3):
    ans += H(n-i,i//3)
ans = (ans % mod + mod) % mod
print(ans)