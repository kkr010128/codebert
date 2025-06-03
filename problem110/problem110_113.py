# input here
_INPUT = """\
2 3 2
..#
###
"""

def main():
    H, W, K = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    n = H + W
    ans = 0
    for i in itertools.product(range(2), repeat=H):
        for j in itertools.product(range(2), repeat=W):
            cnt = 0            
            for y in range(H):
                if i[y]:
                    continue
                for x in range(W):
                    if j[x]:
                        continue
                    if grid[y][x] == "#":
                            cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    import io
    import sys
    import math
    import itertools

    # sys.stdin = io.StringIO(_INPUT)
    main()