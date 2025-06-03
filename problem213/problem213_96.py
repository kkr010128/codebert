import sys

def main():

    N = int(sys.stdin.readline().rstrip())
    X = [int(x) for x in sys.stdin.readline().rstrip().split()]

    m = 100**2 * 100
    for p in range(101):
        tmp = 0
        for x in X:
            tmp += (x - p)**2
        m = min(tmp,m)

    print(m)


main()