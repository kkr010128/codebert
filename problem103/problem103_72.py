import sys
def input():
    return sys.stdin.readline()[:-1]


def main():
    N = int(input())
    A = list(map(int,input().split()))
    zougen = [-1 if A[i] > A[i + 1] else 1 for i in range(N - 1)]
    money = 1000
    kabu = 0
    for i in range(N-1):
        if zougen[i] == 1:
            kabu += money // A[i]
            money = money % A[i]
        else:
            money += kabu * A[i]
            kabu = 0
    print(A[-1] * kabu + money)



if __name__ == "__main__":
    main()