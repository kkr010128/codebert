# 視点を変えてやる全探索 実は条件よりAを全列挙することが可能

# rec, 1からじゃなくて0からにしてたせいか1ケースでWA????

n, m, q = map(int, input().split())
koho = []


def rec(arr):
    if len(arr) == n:
        koho.append(arr)
    else:
        for i in range(arr[-1], m + 1):
            nex_arr = arr[:]
            nex_arr.append(i)
            rec(nex_arr)


# これ 0からにしてたんだけど べつに影響なくないか？？？？？？
for i in range(1, m + 1):
    rec([i])
ans = 0

qs = []
for _ in range(q):
    qs.append(list(map(int, input().split())))

for arr in koho:
    tmp = 0
    for abcd in qs:
        if arr[abcd[1] - 1] - arr[abcd[0] - 1] == abcd[2]:
            tmp += abcd[3]
    ans = max(ans, tmp)
print(ans)