import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
from itertools import combinations_with_replacement
INF = float('inf')

def main():
    N, M, Q = map(int, readline().split())
    abcd = []

    for _ in range(Q):
        a,b,c,d = map(int, readline().split())
        abcd.append([a,b,c,d])

    As = combinations_with_replacement(range(1,M+1),N)
    ans = 0

    for A in As:
        score = 0
        for a,b,c,d in abcd:
            if A[b-1] - A[a-1] == c:
                score += d

        ans = max(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
