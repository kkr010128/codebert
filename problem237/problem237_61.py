N = int(input())
rob = []
for i in range(N):
    X, L = map(int, input().split())
    rob.append([X-L, X+L])
rob.sort(key=lambda x: x[1])
ans = N
for i in range(N-1):
    if rob[i+1][0] < rob[i][1]:
        rob[i+1][1] = rob[i][1]
        ans -= 1
print(ans)