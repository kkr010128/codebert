def fn(x):
    return [x[0], int(x[1])]

N, q = map(int, input().split())
name_time = list(map(fn, [ input().split() for n in range(N) ]))
sec = 0; finish =[];

while True:
    if len(name_time) == 0:
        break
    elif name_time[0][1] > q:
        sec += q
        name_time[0][1] -= q
        name_time.append(name_time.pop(0))
    else:
        sec += name_time[0][1]
        finish.append([name_time.pop(0)[0],sec])
for f in finish:
    print(*f)

