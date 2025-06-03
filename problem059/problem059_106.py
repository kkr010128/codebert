table = []
r,c = [int(x) for x in input().split( )]
for i in range(r):
    mini_table = [int(x) for x in input().split( )]
    table.append(mini_table)
for i in table:
    i.append(sum(i))
gyou = []
for i in range(c+1):
    counter = 0
    for j in range(r):
        counter += table[j][i]
    gyou.append(counter)
table.append(gyou)
for i in table:
    print(' '.join(str(j) for j in i))

