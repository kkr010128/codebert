row, col = map(int, raw_input().split())

ret = []
for _ in range(row):
    _row = map(int, raw_input().split())
    _row += [sum(_row)]
    ret.append(_row)

for i in ret: 
    print ' '.join(map(str, i))

ret_sum = []
for i in range(col+1):
    work = 0
    for j in ret: 
        work += j[i] 
    ret_sum.append(work)

print ' '.join(map(str, ret_sum))