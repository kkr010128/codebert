n = int(input())
m = list(map(int,input().split()))
m.sort()

ans = 0
for i in range(n):
    for j in range(i+1,n):
        l = j
        r = n
        while r-l>1:
            mid = (r+l)//2
            if m[mid] < m[i]+m[j] and m[i] < m[mid]+m[j] and m[j] < m[mid]+m[i]:
                l = mid
            else:
                r = mid
        ans += l-j

print(ans)