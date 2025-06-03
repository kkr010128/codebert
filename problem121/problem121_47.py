N = int(input())

a = [0]

i = 0
L = 26
while True:
    if a[i] < N <= a[i] + L**(i + 1):
        break
    a.append(a[i] + L**(i + 1))
    i += 1


N -= a[i] + 1

for j in range(i, -1, -1):
    if j > 0:
        print(chr(N // L**(j) + ord('a')), end="")
    else:
        print(chr(N + ord('a')), end="")
    N = N % L**(j)
