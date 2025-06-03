import sys
#input = sys.stdin.buffer.readline

def main():
    H,W,K = map(int,input().split())
    s = [list(map(str,input())) for _ in range(H)]
    ans = [[0 for _ in range(W)] for _ in range(H)]
    up,down = 0,1
    count = 1
    for i in range(H):
        if "#" not in s[i]:
            if down != H:
                down += 1
            else:
                for x in range(up,down):
                    for y in range(W):
                        ans[x][y] = ans[up-1][y]
        else:
            now = 0
            for j in range(W):
                if s[i][j] == "#":
                    for x in range(up,down):
                        for y in range(now,j+1):
                            ans[x][y] = count
                    now = j+1
                    count += 1
            if s[i][-1] == ".":
                for x in range(up,down):
                    for y in range(now,W):
                        ans[x][y] = count-1
            up = down
            down += 1
    
    for i in range(H):
        print(*ans[i])

if __name__ == "__main__":
    main()