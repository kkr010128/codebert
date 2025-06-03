import sys


def resolve(in_):
    n, k = map(int, in_.readline().split())
    a = list(map(int, in_.readline().split()))
    mod = 10 ** 9 + 7
    assert n == len(a)
    # print(f'{n=} {k=} {len(a)=}')

    m = sorted(filter(lambda x: x < 0, a))
    p = sorted(filter(lambda x: x >= 0, a), reverse=True)

    if len(p) == 0:
        # print(f'{m=}')
        if k % 2:
            ans = m[-1] % mod
            for v in m[-k:-1]:
                v %= mod
                ans *= v
                ans %= mod
            return ans
        else:
            ans = m[0] % mod
            for v in m[1:k]:
                v %= mod
                ans *= v
                ans %= mod
            return ans
    elif len(m) == 0:
        ans = p[0] % mod
        for v in p[1:k]:
            v %= mod
            ans *= v
            ans %= mod
        return ans

    values = []
    p_index = 0
    m_index = 0
    for _ in range(k):
        if p_index < len(p) and m_index < len(m):
            if p[p_index] >= abs(m[m_index]):
                values.append(p[p_index])
                p_index += 1
            else:
                values.append(m[m_index])
                m_index += 1
        elif p_index >= len(p):
            values.append(m[m_index])
            m_index += 1
        elif m_index >= len(m):
            values.append(p[p_index])
            p_index += 1
        else:
            raise ValueError(f'{p_index=} {m_index=}')
    # print(f'{values[:10]=} {p[:10]=} {m[:10]=}')

    
    if any(v == 0 for v in values):
        return 0
    
    minus_values = sum(1 for v in values if v < 0)
    # print(f'{minus_values > 0 and minus_values % 2=}')
    if minus_values > 0 and minus_values % 2:
        x = None
        y = None
        minus_max = max((value for value in values if value < 0), default=None)
        plus_min = min((value for value in values if value >= 0), default=None)
        if len(p) > p_index and minus_max:
            # print(f'{p[p_index]=}')
            x = abs(p[p_index] + minus_max)
        if len(m) > m_index and plus_min:
            # print(f'{m[m_index]=}')
            y = abs(m[m_index] + plus_min)
        # print(f'{x=} {y=} {minus_max=} {plus_min=}')
        if x is None and y is None:
            pass
        elif x is None or y is None:
            if x is None:
                values.remove(plus_min)
                values.append(m[m_index])
            elif y is None:
                values.remove(minus_max)
                values.append(p[p_index])
        else:
            if x < y:
                values.remove(minus_max)
                values.append(p[p_index])
            elif x > y:
                values.remove(plus_min)
                values.append(m[m_index])
            elif abs(minus_max) < plus_min:
                values.remove(plus_min)
                values.append(m[m_index]) 
            else:
                values.remove(minus_max)
                values.append(p[p_index])
               

    ans = values[0] % mod
    for v in values[1:k]:
        v %= mod
        ans *= v
        ans %= mod
    
    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()