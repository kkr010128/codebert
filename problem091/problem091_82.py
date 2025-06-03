n = int(input())
l = list(map(int, input().split()))

ans = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if l[i] == l[j]:
                continue
            if l[j] == l[k]:
                continue
            if l[i] == l[k]:
                continue
            if max(l[i], l[j], l[k]) * 2 < l[i] + l[j] + l[k]:
                ans += 1

print(ans)