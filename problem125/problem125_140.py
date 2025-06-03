from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def main():
    X = ri()
    K = 360 // gcd(360, X)
    print(K)


if __name__ == '__main__':
    main()
