N, M = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
b = 0

for i in range(M):
    if sum(a)%(M*4)== 0:
        if a[i] >= int(sum(a)/(M*4)):
            b += 1 
    if sum(a)%(M*4)!= 0:
        if a[i] > int(sum(a)//(M*4)):
            b += 1 
if b == M:
    print('Yes')
elif b < M:
    print('No')