N, M = map(int, input().split())

ans = []
if M%2 == 0:
    for i in range(1, M//2+1):
        ans.append([i, M+1-i])
        ans.append([M+i, 2*M+2-i])
else:
    for i in range(1, M//2+1):
        ans.append([i, M+1-i])
    for i in range(1, (M+1)//2+1):
        ans.append([M+i, 2*M+2-i])

for i in range(len(ans)):
    print(*ans[i])