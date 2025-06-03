from sys import exit

N, R = [int(x) for x in input().split()]

if N >= 10:
    print(R)
    exit()
else:
    print(R + (100 * (10 - N)))
    exit()
