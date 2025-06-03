S = input()

l = len(S)
x = [0]*(l+1)
y = [0]*(l+1)
for i in range(l):
    if S[i] == "<":
        x[i+1] = x[i]+1
for i in range(l):
    if S[l-i-1] == ">":
        y[l-i-1] = y[l-i]+1

res = 0
for a, b in zip(x, y):
    res += max(a, b)

print(res)