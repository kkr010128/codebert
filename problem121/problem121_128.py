import math
N = int(input())
digit = math.ceil(math.log((25 * N / 26 + 1), 26))

alphabet = list("abcdefghijklmnopqrstuvwxyz")

name = []

for i in range(digit):
  name.append((N % 26 - 1) % 26)
  N = (N - (N % 26 - 1) % 26) // 26

name.reverse()
print("".join([alphabet[s] for s in name]))
