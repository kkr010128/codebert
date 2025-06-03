import itertools
# H, W = [int(_) for _ in input().split()]
N = int(input())

comb = itertools.combinations_with_replacement([str(i) for i in range(1, 10)], 2)
count = 0
for c in comb:
    A = c[0]
    B = c[1]
    count_1 = 0
    count_2 = 0
    for i in range(1, N+1):
        if str(i)[0] == A and str(i)[-1] == B:
            count_1 += 1
        elif str(i)[0] == B and str(i)[-1] == A:
            count_2 += 1
    if A == B:
        count += count_1 ** 2
    else:
        count += count_1 * count_2 * 2
print(count)
