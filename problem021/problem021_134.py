X = raw_input()
S1 = []
S2 = []
total = 0
for i, x in enumerate(X):
    if x == '\\':
        S1.append(i)
    elif x == '/' and len(S1) > 0:
        left = S1.pop()
        s = i - left
        total += s
        while len(S2) > 0:
            prev = S2.pop()
            if prev[0] < left:
                S2.append(prev)
                break
            else:
                s += prev[1]
        S2.append((left, s))
print total
result = [len(S2)]
for i in S2:
    result.append(i[1])
print ' '.join(map(str, result))