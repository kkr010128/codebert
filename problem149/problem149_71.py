import numpy as np
n,m,x = map(int,input().split())
value = []
books = []
for i in range(n):
    a = list(map(int,input().split()))
    value.append(a[0])
    books.append(np.array(a[1:]))
if min(sum(books))<x:
    print(-1)
else:
    ans = 10**8
    for i in range(2**n):
        M = np.array([0]*m)
        v = 0
        for j in range(n):
            if i >> j & 1:
                M += books[j]
                v += value[j]
        if min(M)>= x:
            ans = min(ans,v)
    print(ans)