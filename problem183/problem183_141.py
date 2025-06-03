from math import sqrt
def div(n):
    s = set()
    for i in range(1, int(sqrt(n))+2):
        if n%i == 0:
            s.add(i)
            s.add(n//i)
    return s

def solve(x, n):
    while n % x == 0:
        n //= x
    if n % x == 1:
        return True
    return False

def main():
    n = int(input())
    t = div(n) | div(n-1)
    ans = 0
    for v in t:
        if v != 1 and solve(v, n):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()