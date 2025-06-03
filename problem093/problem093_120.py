N, K = map(int, input().split())
P_L = [int(x)-1 for x in input().split()]
C_L = [int(x) for x in input().split()]

ans = float("-Inf")
for s in range(N):
    _s_l = []
    _v = s
    _cumsum = 0
    _ans = float("-Inf")
    while True:
        _nextv = P_L[_v]
        _cumsum += C_L[_nextv]
        _s_l.append(_cumsum)
        _v = _nextv
        if _nextv == s:
            break
    if K <= len(_s_l):
        _ans = max(_s_l[:K])
    else:
        if _s_l[-1] < 0:
            _ans = max(_s_l)
        else:
            _l = len(_s_l)
            if K % _l == 0:
                _ans = max(_s_l[-1] * (K // _l),
                           _s_l[-1] * (K // _l - 1) + max(_s_l))
            else:
                _ans = max(_s_l[-1] * (K // _l) + max(_s_l[:K % _l]),
                           _s_l[-1] * (K // _l - 1) + max(_s_l))
    ans = max(ans, _ans)

print(ans)
