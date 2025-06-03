N = int(input())
X_list = list(map(int, input().split()))
X_list_min = sorted(X_list)

ans = 10**8+1

for i in range(X_list_min[0], X_list_min[-1]+1):
    ans_temp = 0
    for j in range(N):
        ans_temp += (X_list_min[j] - i)**2
    ans = min(ans, ans_temp)
print(ans)