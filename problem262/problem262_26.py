from itertools import combinations
n = int(input())
state = [None] + [[set(),set()] for _ in range(n)]

for i in range(1,n+1):
    a = int(input())
    for _ in range(a):
        x,y = map(int,input().split())
        if y == 0:
            state[i][0].add(x)
        if y == 1:
            state[i][1].add(x)

ans = 0
#正直者の人数を仮定
for i in range(1,n+1):
    #正直者の選び方を仮定
    for j in combinations(list(range(1,n+1)), i):
        assum = set(j)
        state_lst = []
        #正直者の証言抽出
        for each_state in j:
            state_lst.append(state[each_state])
        #証言の矛盾を確認
        for each_state in state_lst:
            crr0 = assum.isdisjoint(each_state[0])
            crr1 = assum >= each_state[1]
            crr = crr0 and crr1
            if not crr:
                break
        else:
            ans = i

print(ans)