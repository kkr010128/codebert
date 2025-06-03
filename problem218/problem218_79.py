n = int(input())
s = [input() for _ in range(n)]

s_sort = sorted(s)

s_num = [1]*n

for i in range(1,n):
    if s_sort[i] == s_sort[i-1]:
        s_num[i] += s_num[i-1]

Maxnum = max(s_num)

index_num = [n for n, v in enumerate(s_num) if v == Maxnum]

[print(s_sort[i]) for i in index_num]
