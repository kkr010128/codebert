S = []
A = raw_input().split()

for i in A:
    if i == '+':
        S.append(int(S.pop()) + int(S.pop()))
    elif i == '-':
        S.append(-int(S.pop()) + int(S.pop()))
    elif i == '*':
        S.append(int(S.pop()) * int(S.pop()))
    else:
        S.append(i)

print S[0]