from collections import deque
s = deque(list(input()))
q = int(input())
# -1がnotReverse, 1がReverser
isR = -1
for i in range(q):
    line = list(input().split())
    t = int(line[0])
    if t == 1:
        isR *= -1
    else:
        f = int(line[1])
        if isR + f == 0 or isR + f == 3:
            s.appendleft(line[2])
        else:
            s.append(line[2])
if isR == 1:
        s.reverse()
print("".join(s))