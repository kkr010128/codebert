# C - Guess The Number
N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]

ans = [0,0,0]

# 条件だけで不適がわかるものは弾く
for i in range(M):
    for j in range(i+1,M):
        if (SC[i][0] == SC[j][0]) and (SC[i][1] != SC[j][1]):
            print(-1)
            quit()

# 各桁を指定をする
for k in range(M):
    ans[SC[k][0]-(N-2)] = str(SC[k][1])

# 頭の桁が0で指定されると不適(str型かどうかで判定する)
if (ans[3-N] == "0") and (N == 1):
    print(0)
    quit()
elif ans[3-N] == "0":
    print(-1)
    quit()

# N桁の文字列にする
ans = [str(ans[i]) for i in range(3)]
res = "".join(ans)
res = res[(3-N):4]

# 頭の桁が指定無しの0だったら1に変える
if (res[0] == "0") and (N == 1):
    res = "0"
elif res[0] == "0":
    ref = list(res)
    ref[0] = "1"
    res = "".join(ref)

print(res)
