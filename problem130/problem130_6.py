S = input()
A = ''
P = 0
for s in range(len(S)):
    if P < 3:
        A += S[s]
    P += 1
print(A)