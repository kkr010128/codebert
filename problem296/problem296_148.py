S = input()
K = int(input())

curr = S[0]
tmp = ""
T = []
for s in S:
    if s == curr:
        tmp += s
    else:
        T.append(tmp)
        curr = s
        tmp = s
T.append(tmp)

if len(T) == 1:
    res = (len(S) * K) // 2
    print(res)
    exit(0)

res = 0
t_first = T[0]
t_last = T[-1]

if t_first[0] != t_last[0]:
    res += (len(t_first) // 2) * K
    res += (len(t_last) // 2) * K
else:
    res += len(t_first) // 2
    res += len(t_last) // 2
    res += (len(t_first + t_last) // 2) * (K - 1)

for t in T[1:-1]:
    res += (len(t) // 2) * K

print(res)
