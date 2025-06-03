from string import ascii_lowercase
N = int(input())

k = [0, 26]
for i in range(1, 13):
    k.append(26 * (k[i] + 1))

for i in range(13):
    if k[i] + 1 <= N <= k[i+1]:
        n = N - (k[i] + 1)

        for j in range(i, -1, -1):
            print(ascii_lowercase[(n//26**j) % 26], end="")