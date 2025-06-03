from collections import deque

S = input()


s1 = deque()
s2 = deque()
total = 0

for i, s in enumerate(S):
    if s == '\\':
        s1.append(i)
    elif s == '/':
        if not s1:
            continue
        j = s1.pop()
        total += i - j

        vol = i - j
        while s2 and s2[-1][0] >= j:
            vol += s2.pop()[1]

        s2.append((j, vol))

print(total)
print(len(s2), *[vol for idx, vol in s2])

