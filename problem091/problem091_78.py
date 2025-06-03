import itertools

N = int(input())
L = list(map(int, input().split()))

combinations = list(itertools.combinations(range(N), 3))

count = 0
for cmb in combinations:
    flag = True
    for i in range(3):
        if L[cmb[i]] + L[cmb[(i + 1) % 3]] > L[cmb[(i + 2) % 3]] and L[cmb[i]] != L[cmb[(i + 1) % 3]]:
            continue
        else:
            flag = False
            break
    if flag:
        count += 1

print(count)