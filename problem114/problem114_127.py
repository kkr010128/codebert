
D = int(input())
c_list = list(map(int, input().split()))
s_list = [list(map(int, input().split())) for _ in range(D)]

last_open = [0] * 26
res = 0

res_list = []
for i in range(D):
    t = int(input())
    res += s_list[i][t-1]

    bad = 0
    last_open[t-1] = i+1
    for ci in range(26):
        bad += c_list[ci]*(i+1 - last_open[ci])

    res -= bad
    print(res)
    res_list.append(res)
