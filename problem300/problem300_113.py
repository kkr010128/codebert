import math

def factorization(n):
    d = [1]
    i = 2
    while True:
        if i > int(math.sqrt(n)):
            break
        if n % i == 0:
            d.append(i)
            n //= i
        else:
            i += 1
    if n != 1:
        d.append(n)
    return d


def main():
    A, B = map(int, input().split())
    fa = set(factorization(A))
    fb = set(factorization(B))
    print(len(fa & fb))


if __name__ == '__main__':
    main()
