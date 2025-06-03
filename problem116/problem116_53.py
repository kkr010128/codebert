s,t = input(), input()

S = list(s)
T = list(t)

N = len(s) - 1
i = 0
counter = 0

while N + 1 != i:
    if S[i] != T[i]:
        S[i] = T[i]
        counter += 1
    i += 1

print(counter)