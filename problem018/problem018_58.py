S = []

A = raw_input().split()

for i in range(len(A)):
    if A[i] == '+':
        S.append(int(S.pop()) + int(S.pop()))
    elif A[i] == '-':
        S.append(-int(S.pop()) + int(S.pop()))
    elif A[i] == '*':
        S.append(int(S.pop()) * int(S.pop()))
    else:
        S.append(A[i])

print S[0]