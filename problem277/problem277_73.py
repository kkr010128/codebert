import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
mlmis = lambda: [-int(x) for x in input().split()]
INF = float('inf')
#

def main():
    H,W,K=mis()
    S = [input() for i in range(H)]
    ranges = []
    u = b = 0
    while u < H:
        if '#' in S[b]:
            ranges.append(range(u, b+1))
            u = b = b+1
        elif b == H-1:
            last = ranges.pop()
            ranges.append(range(last[0], H))
            break
        else:
            b += 1
    c = 1
    for ran in ranges:
        l = r = 0
        s = []
        while l < W:
            s.append(c)
            if any(S[i][r]=='#' for i in ran):
                c += 1
                l = r = r+1
            elif r == W-1:
                for i, elem in enumerate(s):
                    if elem == c:
                        s[i] = c-1
                break
            else:
                r += 1
        for _ in ran:
            print(' '.join(map(str, s)))
        


main()
