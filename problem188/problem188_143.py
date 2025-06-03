(x, y, A, B, C) = map(int, raw_input().split())

ps = sorted(map(int, raw_input().split()), reverse=True)[:x]
qs = sorted(map(int, raw_input().split()), reverse=True)[:y]
cs = sorted(map(int, raw_input().split()))

tot = sum(ps) + sum(qs)

while cs and ((ps and cs[-1] > ps[-1]) or (qs and cs[-1] > qs[-1])):
    if ps and qs:
        if ps[-1] < qs[-1]:
            tot -= ps.pop()
            tot += cs.pop()
        else:
            tot -= qs.pop()
            tot += cs.pop()
    elif ps:
        tot -= ps.pop()
        tot += cs.pop()
    elif qs:
        tot -= qs.pop()
        tot += cs.pop()
    else:
        break
# print ps, qs

print tot

