from collections import deque
area = input()
S1 = deque()
S2 = deque()
total = 0

for i, v in enumerate(area):
    if v == '\\':
        S1.append(i)
    elif v == '/' and S1:
        j = S1.pop()
        subtotal = i - j
        total += i - j
        while S2 and S2[-1][0] > j:
            subtotal += S2.pop()[1]
        S2.append([j, subtotal])

print(total)
print(len(S2), *(subtotal for j, subtotal in S2))