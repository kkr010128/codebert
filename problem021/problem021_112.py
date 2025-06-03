from collections import deque
que = deque()
l = input()
S = 0
S2 = []
for j in range(len(l)):
    i = l[j]
    if i == '\\':
        que.append(j)
        continue
    elif i == '/':
        if len(que) == 0:
            continue
        k = que.pop()
        pond_sum = j-k
        S += pond_sum
        while S2 and S2[-1][0] > k:
            pond_sum += S2[-1][1]
            S2.pop()
        S2.append([k,pond_sum])
    elif i == '_':
        continue
data = [i for j,i in S2]
print(S)
print(len(S2),*data)
