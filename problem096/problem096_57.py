def main():
    from sys import stdin
    from math import sqrt

    readline = stdin.readline

    N,D = list(map(int,readline().rstrip().split()))
    count = 0

    for X in range(N):
        X1,X2 = list(map(int,readline().rstrip().split()))
        
        if sqrt(X1**2 + X2**2) <= D :
            count += 1

    print(count)

main()