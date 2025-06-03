f = [1, 1] + [0] * (int(input()) - 1)
for i in range(2, len(f)):f[i] = f[i - 2] + f[i - 1]
print(f[-1])
