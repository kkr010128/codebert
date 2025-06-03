from collections import deque

N, X, Y = map(int, input().split())
ans = [0] * N
for i in range(N-1):
    dist_list = [-1] * N
    d = deque([[i]])
    dist = 0
    while d[0]:
        tag = d.popleft()
        next_tag = []
        for t in tag:
            if dist_list[t] == -1:
                dist_list[t] = dist
            if t - 1 >= 0:
                if dist_list[t - 1] == -1:
                    next_tag.append(t-1)
            if t + 1 < N:
                if dist_list[t + 1] == -1:
                    next_tag.append(t + 1)
            if t == X-1:
                if dist_list[Y-1] == -1:
                    next_tag.append(Y-1)
            if t == Y-1:
                if dist_list[X-1] == -1:
                    next_tag.append(X-1)
        d.append(next_tag)
        dist += 1
    for j in range(i+1, N):
        ans[dist_list[j]] += 1

for i in range(1,N):
    print(ans[i])