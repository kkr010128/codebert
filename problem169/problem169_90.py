N = int(input())
A_ls = list(map(int, input().split(' ')))
rst = [0] * N
for i in A_ls:
    rst[i - 1] += 1
for i in rst:
    print(i)