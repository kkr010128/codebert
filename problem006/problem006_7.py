import sys

def compoundInterest(x, i, n):
    if n == 0:
        return x

    ans = int(x * (1 + i))
    hasu = ans % 1000
    if hasu != 0:
        ans -= hasu
        ans += 1000
    return compoundInterest(ans, i, n-1)

if __name__ == "__main__":
    n = int(input())
    ans = compoundInterest(100000, 0.05, n)
    print (ans)