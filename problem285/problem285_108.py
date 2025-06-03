S = input()
a = [0] * (len(S) + 1)
for i in range(len(S)):
    if S[i] == "<":
        a[i + 1] = a[i] + 1

for i in list(range(len(S)))[::-1]:
    if S[i] == ">" and a[i + 1] >= a[i]:
        a[i] = a[i + 1] + 1

print(sum(a))
