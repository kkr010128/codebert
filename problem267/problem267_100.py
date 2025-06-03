N = int(input())
S = input()
third = [[[False]*10 for _ in range(10)] for __ in range(10)]
second = [[False]*10 for _ in range(10)]
first = [False]*10
for s in S:
    s = int(s)
    for i in range(10):
        if first[i]:
            for j in range(10):
                if second[i][j]:
                    third[i][j][s] = True
            second[i][s] = True
    first[s] = True

res = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if third[i][j][k]:
                # print(i, j, k)
                res += 1
print(res)
