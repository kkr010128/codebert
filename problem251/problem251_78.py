N, K = [int(i) for i in input().split()]
R, S, P = [int(i) for i in input().split()]
d = {'r': P, 's': R, 'p': S}
T = input()
checked = [False for i in range(N)]
# 勝てるだけ勝てばいい
for i in range(N-K):
    if T[i] == T[i+K]:
        if checked[i] == False:
            checked[i+K] = True
result = 0
for i in range(N):
    if checked[i] == False:
        result += d[T[i]]
print(result)