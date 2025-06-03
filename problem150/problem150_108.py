n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [aa-1 for aa in a]
check = [0 for i in range(n)]

count = 0
point = 0
check[0] = 1
path = [0]
for i in range(min(n, k)):
    if i == 0 or check[point] == 0:
        check[point] = i+1
        point = a[point]
        path.append(point)
    else:
        break


cycle_len = len(path)-check[point]
pre = check[point]
if pre > k:
    print(path[k])
else:
    k -= pre
    k %= cycle_len
    print(path[pre+k]+1)
