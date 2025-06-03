import sys
N = int(input())
mod = pow(10, 9)+7
if N < 3:
    print(0)
    sys.exit()
ans = 1
for j in range(2, N//3+1):
    r = j-1
    n = N-j*3+r
    bunshi = 1
    bunbo = 1
    for i in range(r):
        bunshi = (bunshi*(n-i)) % mod
        bunbo = (bunbo*(i+1)) % mod
    ans = (ans+(bunshi*pow(bunbo, -1, mod))) % mod
print(ans)
