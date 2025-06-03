N = int(input())
XY_list = [[] for _ in range(N)]
for i in range(N):
    num = int(input())
    for j in range(num):
        person, state = map(int, input().split())
        XY_list[i].append([person - 1, state])
ans = 0
for i in range(1 << N):
    bool = True
    for j in range(N):
        if (i >> j) & 1 == 1:
            for person, state in XY_list[j]:
                if (i >> person) & 1 != state:
                    bool = False
                    break

    if bool:
        ans = max(ans, bin(i)[2:].count("1"))
print(ans)
