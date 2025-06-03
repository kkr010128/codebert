def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, K = [int(x) for x in input().strip().split()]
    P = [int(x)-1 for x in input().strip().split()]
    C = [int(x) for x in input().strip().split()]
    ans = -float('inf')
    f_cnt = [0] * N
    f_score = [0] * N
    for i in range(N):
        if f_cnt[i]:
            continue
        flag = [False] * N
        q = deque([])
        j = i
        cnt = 0
        score = 0
        while not flag[j]:
            flag[j] = True
            q.append(j)
            score += C[j]
            cnt += 1
            j = P[j]
        for j in q:
            f_cnt[j] = cnt
            f_score[j] = score
    # print(*f_cnt)
    # print(*f_score)

    def f(cur, cnt):
        ret = -float('inf')
        ret_ = 0
        if f_score[cur] >= 0:
            ret_ += f_score[cur] * (cnt // f_cnt[cur] - 1)
            cnt = cnt % f_cnt[cur] + f_cnt[cur]
            ret = ret_
        else:
            cnt = min(cnt, f_cnt[cur])

        while cnt:
            # print('  cur = {}, cnt = {}, ret = {}'.format(cur, cnt, ret_))
            cur = P[cur]
            ret_ += C[cur]
            ret = max(ret, ret_)
            cnt -= 1

        return ret

    for i in range(N):
        # print('i = {}'.format(i))
        ans = max(ans, f(i, K))
    
    print(ans)

if __name__ == '__main__':
    main()
