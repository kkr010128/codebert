N, K = map(int, input().split())
R, S, P = map(int, input().split())
score = {'r': R, 's': S, 'p': P}
T = input()
hand = {'r': 'p', 's': 'r', 'p': 's'}

history = []
cnt = 0
for i, t in enumerate(T):
    if i < K:
        u = hand[t]
        flag = 1
    elif K <= i < N - K:
        l = i - K
        r = i + K
        if hand[t] == history[l]:
            u = T[r]
            flag = 0
        else:
            u = hand[t]
            flag = 1
    else:
        l = i - K
        if hand[t] == history[l]:
            u = t
            flag = 0
        else:
            u = hand[t]
            flag = 1
    cnt += score[u] * flag
    history.append(u)

print(cnt)
