from itertools import product

def max2(x,y):
    return x if x > y else y

N = int(input())
data = [[] for _ in range(N)]
res = 0
for i in range(N):
    for _ in range(int(input())):
        data[i].append(tuple(map(int, input().split())))
for a in product((0,1), repeat=N):
    flg = False
    for i in range(N):
        for x, y in data[i]:
            x -= 1
            if a[i] == 1:
                if a[x] != y:
                    flg = True
                    break
        if flg:
            break
        if i == N-1:
            res = max2(res, sum(a))
print(res)
