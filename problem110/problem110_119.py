info = list(map(int, input().split()))
matrix = [[""] * info[1] for i in range(info[0])]

for i in range(info[0]):
    matrix[i] = list(input())


Black = 0

for i in range(info[0]):
    for j in range(info[1]):
        if matrix[i][j] == "#":
            Black += 1


combination = 0

for i in range(2 ** info[0]):
    non_selected = set()
    count = 0

    for j in range(info[0]):
        if (i >> j) & 1:
            
            for k in range(info[1]):
                if matrix[j][k] == "#":
                    count += 1
        else:
            non_selected.add(j)
    

    for l in range(2 ** info[1]):

        count2 = count
        for t in range(info[1]):
            if (l >> t) & 1:

                for s in non_selected:
                    if matrix[s][t] == "#":
                        count2 += 1

        if (Black - count2) == info[2]:
            combination += 1


print(combination)