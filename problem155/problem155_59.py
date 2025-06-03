#166_C
n, m = map(int, input().split())
h = list(map(int, input().split())) 
a = [0] * m
b = [0] * m

v = [[] for i in range(n)]
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
    v[a[i]].append(h[b[i]])
    v[b[i]].append(h[a[i]])

ans = 0
for i in range(n):
    if v[i] == []:
        ans += 1
    else:
        v[i].sort(reverse=True)
        if h[i] > v[i][0]:
            ans += 1
            
print(ans)