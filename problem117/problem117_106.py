def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    import itertools
    sum_a = list(itertools.accumulate(a))
    sum_b = list(itertools.accumulate(b))
    if sum_a[-1] + sum_b[-1] <= k:
        print(n+m)
        return
    if a[0] > k and b[0] > k:
        print(0)
        return

    for i in range(n):
        if sum_a[i] > k:
            break

    s_a = i - 1
    if sum_a[-1] <= k:
        s_a = n-1
    now_sum = 0
    if s_a >= 0:
        now_sum = sum_a[s_a]
    for i in range(m):
        if now_sum + sum_b[i] > k:
            break
    s_b = i - 1
    ans = s_a + 1 + s_b + 1
    now_sum = 0
    for a_i in range(s_a-1, -2, -1):
        for b_i in range(s_b+1,m):
            if a_i < 0:
                now_sumtime = sum_b[b_i]
            else:
                now_sumtime = sum_a[a_i] + sum_b[b_i]

            if b_i == m-1 and now_sumtime <= k:
                now_sum = a_i + m + 1
                break
            if now_sumtime > k:
                now_sum = a_i + b_i + 1
                break
        s_b = b_i-1
        ans = max(ans, now_sum)
    print(ans)

if __name__=='__main__':
    main()
