n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    answer = []
    for j in range(l):
        answer.append(sum([a[i][k]*b[k][j] for k in range(m)]))
    print(*answer)
        
