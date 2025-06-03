n, m = map(int, input().split(' '))

def nCr(n, r):
    if n < r:
        return 0
    ans = 1
    for i in range (r):
        ans *= (n-r+i+1)
        ans = ans // (i+1)

    return ans

print(nCr(n, 2) + nCr(m, 2))