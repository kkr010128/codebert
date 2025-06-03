from math import gcd


def main():
    K = int(input())
    ans = 0

    for i in range(1, K+1):
        for j in range(1, K+1):
            temp = gcd(i, j)
            for l in range(1, K+1):
                ans += gcd(temp, l)
                
    print(ans)


if __name__ == '__main__':
    main()