S = list(input())
K = int(input())
S.extend(S)

prev = ''
cnt = 0
for s in S:
    if s == prev:
        cnt += 1
        prev = ''
    else:
        prev = s

b = 0
if K % 2 == 0:
    b += 1
if K > 2 and S[0] == S[-1]:
    mae = 1
    while mae < len(S) and S[mae] == S[0]:
        mae += 1
    if mae % 2 == 1 and mae != len(S):
        usiro = 1
        i = len(S) - 2
        while S[i] == S[-1]:
            usiro += 1
            i -= 1
        if usiro % 2 == 1:
            b = K // 2

if K % 2 == 0:
    res = cnt * (K // 2) + (b - 1)
else:
    res = cnt * (K // 2) + cnt // 2 + b
print(res)
