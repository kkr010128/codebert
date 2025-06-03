n, m = map(int,input().split())
lst = [-1 for i in range(n + 1)]
lst[0] = 0
def find(x):
    if(lst[x] < 0):
        return(x)
    else:
        return(find(lst[x]))
def unit(x, y):
    xr = find(x)
    yr = find(y)
    if (xr == yr):
        pass
    else:
        if (xr > yr):
            x, y = y, x
            xr, yr = yr, xr
        lst[xr] = lst[xr] + lst[yr]
        lst[yr] = xr

for i in range(m):
    a, b = map(int,input().split())
    unit(a, b)

print(-(min(lst)))
    
