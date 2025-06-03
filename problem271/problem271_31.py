N = int(input())
S = input()

for s in S:
  print(chr(65+(ord(s)+N-65)%26),end="")