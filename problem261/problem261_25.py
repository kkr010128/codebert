N = input()
n = len(N) // 2
x = N[:n]
y = ''.join(list(reversed(N[-n:])))

count = 0
for i in range(n):
    if x[i] == y[i]:
        continue
    else:
        count += 1

print(count)

