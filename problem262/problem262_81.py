N = int(input())
table = []

for i in range(N):
    A = int(input())
    dic = {}
    for j in range(A):
        x,y = map(int, input().split())
        dic[x-1] = y
    table.append(dic)       

res = 0
for i in range(2**N):
    bi = [j for j in range(N) if (i >> j &1)]
    dic = {}
    for b in bi:
        dic[b] = 1
    
    endfor = False
    for b1 in bi:
        if endfor:
            break
        said = table[b1]
        for k in said.keys():
            if k not in dic.keys():
                if said[k]:
                    endfor = True
                    break
                dic[k] = said[k]
            elif dic[k] == said[k]:
                continue
            else:
                endfor = True
                break
    if not endfor:
        res = max(res, len(bi))

print(res)