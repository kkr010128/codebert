N = int(input())

s = input()

res = 0

search = [("00"+str(s))[-3:] for s in range(0,1000)]

for v in search:
    tmp = s
    if v[0] in tmp:
        tmp = tmp[tmp.index(v[0])+1:]
    else:
        continue
    if v[1] in tmp:
        tmp = tmp[tmp.index(v[1])+1:]
    else:
        continue
    if v[2] in tmp:
        res += 1
print(res)            
