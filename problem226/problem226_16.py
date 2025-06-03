h, n = map(int, input().split())
a = [int(s) for s in input().split()]

a.sort(reverse=True)
ans = 'No'
for s in a:
    h -= s
    if h <= 0:
        ans = 'Yes'
print(ans)