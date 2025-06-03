num_list = []
while True:
    values = [int(x) for x in input().split()]
    if 0 == values[0] and 0 == values[1]:
        break
    num_list.append(values)

for n, t in num_list:
    ret = ' '.join(str(x + y + z) for x in range(1, n + 1) for y in range(x + 1, n + 1) for z in range(y + 1, n + 1))
    cnt = 0
    for x in ret.split():
        if str(t) == x:
            cnt += 1
    print(cnt)