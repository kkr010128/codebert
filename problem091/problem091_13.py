N = int(input())
L = list(map(int, input().split()))
 
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = sorted([L[i], L[j], L[k]])
            if a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
                continue
            if a[0] + a[1] > a[2]:
                ans += 1
 
print(ans)