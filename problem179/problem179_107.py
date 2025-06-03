n, m = map(int,input().split())
a = list(map(int,input().split()))

a.sort(reverse=True)
total = sum(a)
flg = True
for i in range(m):
    if a[i] * 4 * m < total:
        flg = False
        
print('Yes') if flg else print('No')