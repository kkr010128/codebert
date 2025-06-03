n = int(input())
adjacency_list = []
for i in range(n):
    input_list = list(map(int, input().split()))
    adjacency_list.append(input_list[2:])
checked_set = set()
dfs_stack = []
v =[0 for i in range(n)]
f =[0 for i in range(n)]
time = 1
for i in range(n):
    if i not in checked_set:
        dfs_stack = []
        dfs_stack.append(i)
        while dfs_stack:
            current = dfs_stack.pop()
            if current not in checked_set:
                checked_set.add(current)
                v[current] = time
                dfs_stack.append(current)
                for ad in reversed(adjacency_list[current]):
                    if ad-1 not in checked_set:
                        dfs_stack.append(ad-1)
                time +=1
            elif f[current] == 0:
                f[current] = time
                time +=1
for i in range(n):
    print(f'{i+1} {v[i]} {f[i]}')
