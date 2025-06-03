def table_composition(N):
    table = []
    i = 1
    while i <= N/2:
        if N%i == 0:
            table.append(i)
        i += 1
    table.append(N)
    return table

a, b, c = map(int, input().split())
table = table_composition(c)
count = 0
for ele in table:
    if ele >= a and ele <= b:
        count += 1
print(count)