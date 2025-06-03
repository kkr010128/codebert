import math

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

if __name__ == "__main__":
    N = int(input())
    ans = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            x = math.gcd(i, j)
            if(x==1):
                ans += N
            else:
                for k in range(1, N+1):
                    ans += math.gcd(x, k)

    print(ans)
