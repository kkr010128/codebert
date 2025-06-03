import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    N = int(input())
    sDict = defaultdict(int)
    maxCount = 0
    for i in range(N):
        s = input().strip("\n")
        sDict[s] += 1
        maxCount = max(maxCount, sDict[s])
    maxS = []
    for key in sDict:
        if sDict[key] == maxCount:
            maxS.append(key)
    maxS.sort()
    print(*maxS, sep="\n")

    return 0

if __name__ == "__main__":
    solve()