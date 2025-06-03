from math import gcd
def main():
    ans = 0
    k = int(input())
    for i in range(1,1+k):
        for j in range(1,1+k):
            for l in range(1,1+k):
                ans += gcd(i,gcd(j,l))
    print(ans)


if __name__ == "__main__":
    main()