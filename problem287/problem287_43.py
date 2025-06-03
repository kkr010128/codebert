integer = int(input())
for i in range(9):
    for j in range(9):
        if (i + 1) * (j + 1) == integer:
            print('Yes')
            exit()
print('No')