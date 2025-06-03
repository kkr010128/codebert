# -*- coding: utf-8 -*-

N = int(input())
S = input()

ans = 0
for i in range(1000):
    pw = list("{0:03d}".format(i))

    if pw[0] in S:
        w1 = S.index(pw[0])
        if pw[1] in S[w1+1:]:
            w2 = w1+1 + S[w1+1:].index(pw[1])
            if pw[2] in S[w2+1:]:
                ans += 1

print(ans)
