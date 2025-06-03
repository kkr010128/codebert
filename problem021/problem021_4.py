# -*- coding: utf-8 -*-
modelmap = list(input())
S1 = []
S2 = []
A = 0

for i, l in enumerate(modelmap):
    if l == "\\":
        S1.append(i)
    elif l == "/" and len(S1) > 0:
        ip = S1.pop()
        A += i - ip
        L = i - ip
        while len(S2) > 0 and S2[-1][0] > ip:
            L += S2.pop()[1]
        S2.append([ip, L])

print(A)
text2 = "{}".format(len(S2))
for s in S2:
    text2 += " " + str(s[1])
print(text2)            