N, M = map(int, input().split())
corret_list = [False] * (N+1)
wa_number = [0] * (N+1)
true_ans = 0
penalty = 0
for _ in range(M):
    P, S = input().split()
    P = int(P)
    if S == 'AC':
        if not corret_list[P]:
            true_ans += 1
            corret_list[P] = True
            continue
        else:
            continue
    else:
        if not corret_list[P]:
            wa_number[P] += 1
            continue
for i in range(len(corret_list)):
    if corret_list[i]:
        penalty += wa_number[i]
print(true_ans, penalty)