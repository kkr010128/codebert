N = int(input())
query = []
ans = 0

for i in range(N):
    A = int(input())
    query.append([list(map(int, input().split())) for j in range(A)])

for i in range(1<<N):
    count = 0
    FLG = True
    for j in range(N):
        if (i >> j) & 1:
            count += 1
            for x, y in query[j]:
                if (i >> (x - 1)) & 1 != y:
                    FLG = False
                    break   
        if not FLG:
            break
    else:
        ans = max(ans, count)

print(ans)
