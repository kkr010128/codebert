import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

# あるbit列に対するコストの計算
def count(zerone):
    one = 0
    cnt = 0
    for i in range(N):
        flag = True
        if zerone[i] == 1:
            one += 1
            for j in range(len(A[i])):
                if A[i][j][1] != zerone[A[i][j][0]-1]:
                    flag = False
                    break
        if flag:
            cnt += 1
    if cnt == N:
        return one
    else:
        return 0

# bit列の列挙
def dfs(bits):
    if len(bits) == N:
        return count(bits)
    res = 0
    for i in range(2):
        bits.append(i)
        res = max(res, dfs(bits))
        bits.pop()
    return res

# main
N = int(input())
A = [[] for _ in range(N)]
for i in range(N):
    a = int(input())
    for _ in range(a):
        A[i].append([int(x) for x in input().split()])

ans = dfs([])
print(ans)