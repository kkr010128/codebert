N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

scores = {'r': P, 's': R, 'p': S, 'default': 0}
win_flag = [False]*(N+1)
ans = 0

# Kの剰余で別々に考えていい
for i_k in range(K):
    prev = 'default'
    for i_n in range(i_k, N, K):
        # K個前と違う手 もしくは K個前で勝たないことにした 場合
        #   => 点がもらえる
        if (T[i_n] != prev) or (not win_flag[i_n-K]):
            win_flag[i_n] = True
            ans += scores[T[i_n]]
        prev = T[i_n]

print(ans)