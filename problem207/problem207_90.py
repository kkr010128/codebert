import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

bingo = [list(mapint()) for _ in range(3)]
N = int(input())
card = [[0]*3 for _ in range(3)]
for _ in range(N):
    n = int(input())
    for i in range(3):
        for j in range(3):
            if n==bingo[i][j]:
                card[i][j] = 1

for i in range(3):
    if sum(card[i])==3:
        print('Yes')
        exit()

for i in range(3):
    if card[0][i]+card[1][i]+card[2][i]==3:
        print('Yes')
        exit()

if card[0][0]+card[1][1]+card[2][2]==3 or card[2][0]+card[1][1]+card[0][2]==3:
    print('Yes')
    exit()
print('No')