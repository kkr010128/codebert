h,n = map(int,input().split())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
for i in range(n):
    a[i],b[i] = map(int,input().split())
cost = [int(1e+9) for _ in range(h+1)]
cost[0] = 0
for i in range(h):
    for j in range(n):
        if i+a[j] <= h:
            cost[i+a[j]] = min(cost[i+a[j]],cost[i]+b[j])
        else:
            cost[-1] = min(cost[-1],cost[i]+b[j])
print(cost[-1])