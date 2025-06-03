import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    P = [input().strip("\n").split() for _ in range(N)]
    X = input().strip("\n")
    sec = 0
    lastId = 0
    for i in range(N):
        if P[i][0] == X: 
            lastId = i
            break
    for i in range(lastId + 1, N):
        sec += int(P[i][1])
    print(sec)
    
    return 0

if __name__ == "__main__":
    solve()