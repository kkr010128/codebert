from collections import deque

areas = input()
S1 = deque([])
S2 = deque([])

sum_ = 0

for i,ch in enumerate(areas):
    if ch == "\\":
        S1.append(i)
    elif ch == "/" and len(S1) > 0:
        j = S1.pop()
        sum_ += i-j
        a = i-j
        while len(S2) > 0 and S2[-1][0] > j:
            a += S2.pop()[1]
        S2.append([j,a])

ans = []
while len(S2) > 0:
    ans.append(S2.pop()[1])

ans.reverse()

A = sum(ans)
print(A)

ans.insert(0,len(ans))
L = map(str,ans)
print(" ".join(L))
