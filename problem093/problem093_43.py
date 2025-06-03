n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = -float('inf')
for i in range(n):
    s = []
    j = p[i]-1 
    s.append(c[j])
    while j != i:
        j = p[j]-1
        s.append(s[-1]+c[j])
    l = len(s)
    if k <= l:
        a = max(s[:k])
    elif s[-1] <= 0:
        a = max(s)
    else:
        w, r = divmod(k, l)
        a1 = s[-1]*(w-1) + max(s)
        a2 = s[-1]*w
        if r != 0:
            a2 += max(0, max(s[:r]))
        a = max(a1, a2)
    ans = max(ans, a)
print(ans)