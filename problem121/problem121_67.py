N = int(input())
S = ""

while 0<N:
  N-=1
  S+=chr(97+N%26)
  N//=26

print(S[::-1])