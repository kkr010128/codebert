alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
N = int(input())
S = input()
for i in S:
  print(alphabet[(alphabet.index(i)+N) % 26], end='')