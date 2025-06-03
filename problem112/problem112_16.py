num = (10 ** 9) + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))

plus = []
minus = []
zero = 0
ans = 1

for i in a:
    if i > 0:
        plus.append(i)
    elif i < 0:
        minus.append(-i)
    else:
        zero += 1

plus.sort()
minus.sort()
p_l = len(plus)
m_l = len(minus)
cnt = 0


def tail_num(p):
    return p[-1] * p[-2]


if k == 1:
    print(max(a) % num)
elif zero > n - k:
    print(0)
elif zero == n - k:
    for i in plus:
        ans = (i * ans) % num
    for j in minus:
        ans = (ans * j) % num
    if m_l % 2 == 0:
        print(ans)
    else:
        print(-ans % num)
elif len(plus) == 0:
    if k % 2 == 0:
        for j in range(k):
            ans = ans * (minus[-(j + 1)]) % num
        print(ans % num)
    else:
        if 0 in a:
            print(0)
        else:
            for j in range(k):
                ans = ans * (minus[j]) % num
            print(-ans % num)
else:
    if k % 2 == 1:
        ans = ans * plus.pop() % num
        p_l -= 1
    for i in range(k//2):
        if p_l >= 2 and m_l >= 2:
            if tail_num(minus) >= tail_num(plus):
                ans = ans * tail_num(minus) % num
                minus.pop()
                minus.pop()
                m_l -= 2
            else:
                ans = ans * tail_num(plus) % num
                plus.pop()
                plus.pop()
                p_l -= 2
        else:
            if p_l <= 1:
                ans = ans * tail_num(minus) % num
                minus.pop()
                minus.pop()
                m_l -= 2
            else:
                ans = ans * tail_num(plus) % num
                plus.pop()
                plus.pop()
                p_l -= 2
    print(ans)

