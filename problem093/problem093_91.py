n, k = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))
c = list(map(int, input().split()))
    
visited = [False] * n
ans = max(c)

for i in range(n):
    if visited[i]:
        continue
    arr = []
    u = i
    while not visited[u]:
        arr.append(c[u])
        visited[u] = True
        u = p[u]
    s = sum(arr) * (k // len(arr))
    rem = k % len(arr)
    if k // len(arr) >= 1:
        s -= sum(arr)
        rem += len(arr)
        
    arr += arr + arr
    pref_sum = [0]
    for i in arr:
        pref_sum.append(pref_sum[-1] + i)
    # print(pref_sum, s, rem) 
            
    for f in range(len(arr) // 2):
        # ans = max(ans, s + sum(arr[f:f + rem])) 
        for g in range(f + 1, len(pref_sum)):
            if g - f <= k:
                ans = max(ans, pref_sum[g] - pref_sum[f])
            if g - f <= rem:
                ans = max(ans, s + pref_sum[g] - pref_sum[f])
print(ans)
    
