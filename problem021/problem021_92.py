S1 = []
S2= []
sum = 0
for i, s in enumerate(input()):
    if s == "\\":
        S1.append(i)
    elif s == "/" and len(S1) > 0:
        j = S1.pop()
        sum += i - j
        a = i - j
        while len(S2) > 0 and S2[-1][0] > j:
            a += S2.pop()[1]
        S2.append((j, a))
print(sum)
sum2 = [str(len(S2))]
for s in S2:
    sum2.append(str(s[1]))
print(" ".join(sum2))

