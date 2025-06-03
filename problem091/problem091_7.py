from itertools import combinations

N = int(input())
L = list(map(int, input().split()))

count = 0
for C in combinations(L, 3):
    l_list = list(C)
    l_list.sort()

    if l_list[2] > l_list[1] and l_list[1] > l_list[0]:
        if l_list[2] < l_list[1] + l_list[0]:
            count += 1

print(count)