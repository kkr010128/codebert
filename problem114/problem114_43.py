D = int(input())

c = list(map(int, input().split()))

#増加する満足度表 [日数][種類]
s = []
for i in range(D):
    l = list(map(int, input().split()))
    s.append(l)

#開催するコンテストタイプ[日数]
t = [int(input()) for j in range(D)]

last = [0]*26 #最後に開催した日

SP = 0
dis = 0

for k in range(D): #満足度の計算
    SP += s[k][t[k]-1]
    last[t[k]-1] = k + 1 #開催日の更新
    for m in range(26):
        SP -= c[m] * (k + 1 - last[m])
    print(SP)