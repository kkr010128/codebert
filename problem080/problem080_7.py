n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
z = [0] * n
w = [0] * n
for i in range(n):
    z[i] = x[i] + y[i]
    w[i] = x[i] - y[i]
cand1 = max(z) - min(z)
cand2 = max(w) - min(w)
print(max(cand1, cand2))
