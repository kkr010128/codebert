X, N = map(int,input().split())
p_n = list(map(int,input().split()))

p = list(range(102))

for i in p_n:
    for j in range(len(p)):
        if p[j] == i:
            p.pop(j)
            break
            

p_X = list(map(lambda x: x - X, p))
p_abs = list(map(abs,p_X))

print(p[p_abs.index(min(p_abs))])