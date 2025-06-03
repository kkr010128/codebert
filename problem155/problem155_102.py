N, M = map(int, input().split(' '))
H_ls = list(map(int, input().split(' ')))
edge = [ [] for i in range(N) ]
rst = 0
for i in range(M):
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
for i in range(N):
    is_peak = True
    for j in edge[i]:
        if H_ls[i] <= H_ls[j]:
            is_peak = False
            break
    if is_peak:
        rst += 1
print(rst)