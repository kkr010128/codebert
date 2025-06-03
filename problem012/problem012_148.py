import math

def isPrime(x) :
    if x == 2 :
        return True

    if x < 2 or x % 2 == 0 :
        return False

    i = 3
    while i <= math.sqrt(x) :
        if x % i == 0 :
            return False
        i += 2

    return True


def main() :
    n = int(input())
    nums = []
    for i in range(n) :
        x = int(input())
        nums.append(x)

    print(sum(map(isPrime, nums)))


if __name__ == '__main__' :
    main()