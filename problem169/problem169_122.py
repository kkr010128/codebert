import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())
    
    C = [0] * N
    for a in A:
        C[a-1] += 1
    
    print(*C, sep='\n')
    return


if __name__ == '__main__':
    main()
