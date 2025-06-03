n = int(input())
A = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    u, k, *v = list(map(int, input().split()))
    for j in v:
        A[int(u)-1][int(j)-1] = 1
        # A[int(j)-1][int(u)-1] = 1

# for row in A:
#     msg = ' '.join(map(str, row))
#     # print(msg)

d = [-1] * n
f = [-1] * n

t = 0

# recursive


def dfs(u):
    global t
    # print('visit:', str(u), str(t))
    t += 1
    d[u] = t
    for i in range(len(A[u])):
        if A[u][i] == 1 and d[i] == -1:
            dfs(i)
    t += 1
    f[u] = t
            


for i in range(n):
    if d[i] == -1:
        # print('start from:', str(i))
        dfs(i)


for i in range(n):
    print(str(i+1), str(d[i]), str(f[i]))
