import itertools
a,b,c=map(int, input().split())
l = [input() for i in range(a)]

ans = 0
Ans = 0
for i in itertools.product((1,-1),repeat=a):
    for j in itertools.product((1,-1),repeat=b):
        for k in range(a):
            for m in range(b):
                if i[k] == j[m] == 1 and l[k][m] == '#':
                    ans += 1
        if ans == c:
            Ans += 1
        ans = 0
print(Ans)