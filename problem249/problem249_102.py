import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, K = map(int, readline().split())
    if A>=K:
        A -= K
    else:
        B = max(B-(K-A),0)
        A = 0
    print(A, B)



if __name__ == '__main__':
    main()
