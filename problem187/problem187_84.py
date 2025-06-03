N, X, Y = map(int, input().split())
ans = [0]*(N-1)

def cal_dis(i, j):
    return min(j-i, abs(i-X)+abs(j-Y)+1)

for i in range(1, N+1):
    for j in range(i+1, N+1):
        k = cal_dis(i, j)
        ans[k-1] += 1

print('\n'.join(map(str, ans)))

