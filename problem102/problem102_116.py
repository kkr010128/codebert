import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007

def calcSum(n, A):
    return n

def main():
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))

    for i in range(K + 1, N + 1): # K + 1 から N までのループ
        if (A[i - K - 1] < A[i - 1]):
            print("Yes")
        else:
            print("No")
    return

if __name__ == '__main__':
    main()
