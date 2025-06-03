import math
A, B, N = map(int,input().split(' '))

def f(x):
    return math.floor(A*x/B)-A*math.floor(x/B)


def main():
    if N >= B:
        print(f(B-1))
    else:
        print(f(N))

if __name__ == "__main__":
    main()
