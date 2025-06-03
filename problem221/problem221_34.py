S = input()
for i in range(len(S)):
    tmp = S[i]
    S = S.replace(tmp,"x")
print(S)