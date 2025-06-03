S = input()
T = input()
i=0
j=0
for i in range (len(S)):
    if S[i] != T[i]:
        j += 1

print(j)