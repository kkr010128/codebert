S = []

W = raw_input().split()
    
for word in W:
    if word == "+":
        s1 = S.pop()
        s2 = S.pop()
        S.append(s1 + s2)
    elif word == "-":
        s1 = S.pop()
        s2 = S.pop()
        S.append(s2 - s1)
    elif word == "*":
        s1 = S.pop()
        s2 = S.pop()
        S.append(s2 * s1)
    else:
        S.append(int(word))

print S.pop()