import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

cnt = 0
p_cnt = 0
q_cnt = 0
n_list = [i for i in range(1, n+1)]
for P in itertools.permutations(n_list):
    cnt += 1
    if p == list(P):
        p_cnt = cnt
    if q == list(P):
        q_cnt = cnt
    if p_cnt and q_cnt:
        print(abs(q_cnt-p_cnt))
        exit()