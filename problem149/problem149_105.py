n, m, x = map(int, input().split())
#n,m,x,i,j,l,money,k,o
books = []
for i in range(n):
    books.append(list(map(int, input().split())))

ans = 10 ** 10000
import itertools
for i in range(n+1):
    for j in itertools.combinations(books, i):#j:組み合わせ
        l = [0] * m
        money = 0
        for k in j:
            money += k[0]
            for o in range(1, m + 1):
                l[o-1] += k[o]

        if all(a >=x for a in l):
            if money < ans:
                ans = money

if ans == 10 ** 10000:
    print(-1)
else:
    print(ans)
