N = int(input())
L = list(map(int, input().split()))
count = 0
L_sort = sorted(L)
length = len(L_sort)
# 最長辺以外の辺の長さの和 > 最長辺の辺の長さ のとき三角形が成り立つ

for i in range(0, length-2):
    for j in range(i+1, length-1):
        if L_sort[i] == L_sort[j]:
            continue
        for k in range(j+1, length):
            if L_sort[j] == L_sort[k]:
                continue
            if L_sort[i] + L_sort[j] > L_sort[k]:
                count += 1
print(count)