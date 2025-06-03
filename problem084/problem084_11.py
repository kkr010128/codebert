N, M = map(int, input().split())

if M == 0:
    print(1)
    exit()

group_list = []
group_index = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    if group_index[a-1] == 0 and group_index[b-1] == 0:
        group_index[a-1] = len(group_list) + 1
        group_index[b-1] = len(group_list) + 1
        group_list.append(set([a, b]))

    elif group_index[a-1] == 0:
        group_index[a-1] = group_index[b-1]
        group_list[group_index[b-1] - 1].add(a)

    elif group_index[b-1] == 0:
        group_index[b-1] = group_index[a-1]
        group_list[group_index[a-1] - 1].add(b)

    elif group_index[a-1] != group_index[b-1]:
        if len(group_list[group_index[a-1] - 1]) > len(group_list[group_index[b-1] - 1]):
            group_id_b = group_index[b-1] - 1
            for p in group_list[group_id_b]:
                group_index[p-1] = group_index[a-1]
                group_list[group_index[a-1] - 1].add(p)
            group_list[group_id_b] = set()
        else:
            group_id_a = group_index[a-1] - 1
            for p in group_list[group_id_a]:
                group_index[p-1] = group_index[b-1]
                group_list[group_index[b-1] - 1].add(p)
            group_list[group_id_a] = set()

print(max([len(g) for g in group_list]))