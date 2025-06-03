n = int(input())
l =list(map(int, input().split()))
ans = 0
for i in range(n):
        for j in range(i+1, n):
                for k in range(j+1, n):
                        if j > n-2 or k > n-1:
                                continue
                        if l[i] == l[j] or l[j] == l[k] or l[k] == l[i]:
                                continue
                        if abs(l[j] - l[k]) < l[i] < l[j] + l[k]:
                                ans += 1
print(ans)