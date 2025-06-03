n, k = map(int, input().split())

lists = []
for _ in range(k):
    d = int(input())
    having = list(map(int, input().split()))
    for i in having:
        lists.append(i)

sets = set(lists)
ans = n - len(sets)
print(ans)