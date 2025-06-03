N, M = map(int, input().split())

pairs = [[] for _ in range(N + 1)]  # pairs[i]:iと直接つながっている部屋のリスト
for _ in range(M):
    input_list = list(map(int, input().split()))
    pairs[input_list[0]].append(input_list[1])
    pairs[input_list[1]].append(input_list[0])

ans = [0 for _ in range(N + 1)]
n_ans = 0   # ansを埋めた回数 -> N-1になったら終了
done = [False for _ in range(N + 1)]  # 探索済リスト
todo = [1]

while n_ans < N - 1:
    for n in todo:
        for m in pairs[n]:
            if not done[m]:
                done[m] = True
                ans[m] = n
                n_ans += 1
                todo.append(m)

print('Yes')
for i in range(2, N + 1):
    print(ans[i])