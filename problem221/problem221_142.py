S = input()
S = list(S)
x = 'x'
for i in range(len(S)):
    S[i] = x
print("".join(S))