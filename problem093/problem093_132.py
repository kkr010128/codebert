def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10
    N,K = LMIIS()
    P = list(map(lambda x: int(x)-1,input().split()))
    C = LMIIS()
    score_sets = []
    used = [False]*N
    tmp = P[0]
    for i in range(N):
        if not used[i]:
            tmp = i
            score_set = []
            while not used[tmp]:
                used[tmp] = True
                tmp = P[tmp]
                score_set.append(C[tmp])
            score_sets.append(score_set)
        
    ans = -INF
    for score_set in score_sets:
        # 合計が最大になる区間を探す
        len_set = len(score_set)
        sum_score_set_real = sum(score_set)
        sum_score_set = max(0,sum_score_set_real)


        
        for i in range(len_set):
            cum_sum_1 = 0
            for j in range(i,min(len_set, i+K)):
                cum_sum_1 += score_set[j]
                num_move = j-i+1
                tmp_max = cum_sum_1 + (K - num_move) // len_set * sum_score_set
                ans = max(ans, tmp_max)

        for i in range(1,len_set-1):
            cum_sum_2 = sum_score_set_real
            for j in range(i,min(len_set-1-(K-i),len_set-1)):
                cum_sum_2 -= score_set[j]
            for j in range(max(i,len_set-1-(K-i)),len_set-1):
                cum_sum_2 -= score_set[j]
                num_move = len_set - (j-i+1)
                tmp_max = cum_sum_2 + (K - num_move) // len_set * sum_score_set
                ans = max(ans,tmp_max)






        
                
    print(ans)

    
main()
