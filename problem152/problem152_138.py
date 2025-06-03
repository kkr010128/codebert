def check(pt, brackets):
    brackets.sort(reverse=True)
    for m, t in brackets:
        if pt + m < 0:
            return -1
        pt += t
    return pt


n = int(input())
brackets_p = []  # (始めを0として、( = +1, ) = -1 として、最後はいくつか, 途中の最小値はいくつか)
brackets_m = []
pt = 0
mt = 0
for _ in range(n):
    s = input()
    total = 0
    mini = 0
    for c in s:
        if c == '(':
            total += 1
        else:
            total -= 1
            mini = min(mini, total)

    if total >= 0:
        if mini == 0:
            pt += total
        else:
            brackets_p.append((mini, total))
    else:
        total, mini = -total, mini - total
        if mini == 0:
            mt += total
        else:
            brackets_m.append((mini, total))

pt = check(pt, brackets_p)
mt = check(mt, brackets_m)

if (pt == -1) or (mt == -1) or (pt != mt):
    print('No')
else:
    print('Yes')
