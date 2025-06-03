N = int(input())
S = list(input())


for i in range(len(S)):
    S[i] = ord(S[i])

for i in range(len(S)):
    if S[i] + N <= 90:
        S[i] = chr(S[i] + N)
    else:
        S[i] = chr(64 + S[i] + N - 90)


S = ''.join(S)
print(S)