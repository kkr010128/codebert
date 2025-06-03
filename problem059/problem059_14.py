r, c = map(int, input().split())
args = []

for i in range(r):
    args.append(list(map(int, input().split())))
    r_sum = 0
    for j in args[i]:
        r_sum += j
    args[i].append(r_sum)

l_row = []

for k in range(c + 1):
    c_sum = 0
    for l in range(r):
        c_sum += args[l][k]
    l_row.append(c_sum)        

for m in range(r):
    print(' '.join(map(str, args[m])))

print(' '.join(map(str, l_row)))

    

