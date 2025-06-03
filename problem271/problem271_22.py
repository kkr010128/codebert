N = int(input())
S = input()
revALPH = "".join(list(reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))
A = ""

for s in S:
    pos = revALPH.find(s)
    A += revALPH[pos - N]

print(A)