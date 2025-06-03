S = input()
T = input()
if len(S) != len(T): quit()
sum = 0
for i in range(len(S)):
    if T[i] != S[i]:
        sum = sum + 1
print(sum)