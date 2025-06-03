def abc150c_count_order():
    import bisect, itertools
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    pattern = list(itertools.permutations(range(1, n+1)))
    p_idx = bisect.bisect(pattern, p)
    q_idx = bisect.bisect(pattern, q)
    print(abs(p_idx-q_idx))
abc150c_count_order()