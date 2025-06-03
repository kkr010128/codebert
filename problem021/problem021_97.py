line = input()
stack, edges, pools = [], [], []

for i in range(len(line)):
    if line[i] == '\\':
        stack.append(i)
    elif line[i] == '/' and stack:
        j = stack.pop()
        tmp = i - j
        while edges and edges[-1] > j:
            edges.pop()
            tmp += pools.pop()
        edges.append(j)
        pools.append(tmp)

print(sum(pools))
print(len(pools), *pools)