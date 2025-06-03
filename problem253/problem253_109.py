import sys
import time
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, A, B = map(int, readline().split())
    if (B-A)%2==0:
        ans = (B-A)//2
    else:
        left = A-1
        right = N-B
        if left<=right:
            l = left + 1
            ans = l + (B-l)//2
        else:
            r = right + 1
            ans = r + (N-(A+r))//2
    print(ans)

if __name__ == '__main__':
    main()