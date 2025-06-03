from collections import Counter

S1 = input()
K = int(input())
S1C = Counter(S1)
if len(S1C) == 1:
    print(len(S1) * K // 2)
    exit()

start = S1[0]
end = S1[-1]
now = S1[0]
a1 = 0
flag = False
for s in S1[1:]:
    if flag:
        flag = False
        now = s
        continue
    else:
        if s == now:
            a1 += 1
            flag = True
        now = s
S2 = S1 + S1

start = S2[0]
end = S2[-1]
now = S2[0]
a2 = 0
flag = False
for s in S2[1:]:
    if flag:
        flag = False
        now = s
        continue
    else:
        if s == now:
            a2 += 1
            flag = True
        now = s
b = a2 - 2 * a1

print(a1 * K + b * (K-1))