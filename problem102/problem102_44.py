n ,k = map(int, input().split())
lis = list(map(int, input().split()))

 
for i in range(k, n):
    l = lis[i-k]
    r = lis[i]
    if r > l:
        print('Yes')
    else:
        print('No')