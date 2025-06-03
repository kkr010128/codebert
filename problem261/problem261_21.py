S = input()

Sr = S[ : : -1]

hug = 0
for i in range(len(S)):
    if S[i] != Sr[i]:
        hug += 1

print((hug + 1) // 2)