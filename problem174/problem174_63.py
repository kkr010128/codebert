import math


def main():
    K = int(input())
    s = 0
    for i in range(K):
        for j in range(K):
            tmp = math.gcd(i+1, j+1)
            for k in range(K):
                s += math.gcd(tmp, k+1)

    print(s)


if __name__=="__main__":
    main()
