import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readlines
infty = 2 ** 20

lines = input()

n, m = list(map(int, lines[0].split()))

coin = list(map(int, lines[1].split()))

T = [[0] * (n+1) for i in range(m+1)]

#0行目の初期化
for i in range(1, n+1):
    T[0][i] = infty
#0列目の初期化
for i in range(m+1):
    T[i][0] = 0
#1行目の初期化
for i in range(1, n+1):
    T[1][i] = i

cnt = 0
for i in range(1, m+1):
    if coin[i-1] > n:
        continue
    else:
        cnt += 1
        for j in range(1, n+1):
            if j < coin[i-1]:
                T[i][j] = T[i-1][j]
            else:
                a = T[i-1][j] ; b = T[i][j-coin[i-1]]+1
                if a < b:
                    T[i][j] = a
                else:
                    T[i][j] = b

print(T[cnt][n])
