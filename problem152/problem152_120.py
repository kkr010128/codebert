N = int(input())

def cnt(s):
    r = [0] * (len(s)+1)
    for i, v in enumerate(s):
        if v == '(':
            r[i+1] = r[i] + 1
        else:
            r[i+1] = r[i] - 1
    return r[0], r[-1], min(r)

# S1 := 始点 < 終点
S1 = []
# S2 := 始点 => 終点
S2 = []
for i in range(N):
    s = input()
    t = tuple(cnt(s))
    if t[1] > 0:
        S1.append(t)
    else:
        S2.append(t)
def main():
    # Sの終点を合計して0じゃなかったら、終わり
    if sum([s[1] for s in S1]) + sum([s[1] for s in S2]) != 0:
        print("No")
        return
    # S1の中で、最小値が大きい順に並べる
    X1 = sorted(S1, key=lambda x: x[2], reverse=True)
    # S2の中で、最小値が小さい順に並べる
    X2 = sorted(S2, key=lambda x: x[2]-x[1])
    T = 0
    # X1を並べきった後に、X2を並べて実現可能か調べる、終点を合計して0になることは確認済み
    for s, t, mi in X1:
        if T + mi < 0:
            print("No")
            return
        T += t
    for s, t, mi in X2:
        if T + mi < 0:
            print("No")
            return
        T += t
    print("Yes")

main()
