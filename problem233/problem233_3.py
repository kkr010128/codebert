N = int(input())
P = list(map(int, input().split()))

Q = []
for i in range(N):
    if i == 0:
        Q.append(P[i])
    else:
        Q.append(min(Q[-1], P[i]))

cnt = 0
for i in range(N):
    if P[i] <= Q[i]:
        cnt += 1
print(cnt)