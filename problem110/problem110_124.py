import sys
input = sys.stdin.readline

def main():
    H, W, K = map(int, input().split())
    c = [input() for i in range(H)]

    ans = 0
    for maskR in range(2 ** H):
        for maskC in range(2 ** W):
            black = 0
            for i in range(H):
                for j in range(W):
                    if ((maskR >> i) & 1) and ((maskC >> j) & 1) and c[i][j] == '#':
                        black += 1
                    
            if black == K:
                ans += 1
            
    print(ans) 

main()