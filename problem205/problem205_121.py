n, p = map(int, input().split())
s = [int(i) for i in input()]
p_cnt = 0

if p == 2 or p == 5:
    for i in range(n):
        if s[i] % p == 0:
            p_cnt += i+1
        
else:
    s = s[::-1]
    div_dic = dict(zip(range(p), [0] * p))
    tmp = 0

    for i in range(n):
        tmp += s[i] * pow(10, i, p)
        tmp %= p
        div_dic[tmp] += 1

    for v in div_dic.values():
        p_cnt += v * (v - 1)
    p_cnt //= 2
    p_cnt += div_dic.get(0)

print(p_cnt)