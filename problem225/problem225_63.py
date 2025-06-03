import sys
import math
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    H, A = map(int, readline().split())
    print(math.ceil(H/A))

if __name__ == '__main__':
    main()