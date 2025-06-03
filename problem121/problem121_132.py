N = int(input())

alph = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',\
     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',\
         'x', 'y']

seq = []

while N > 0:
    s = N % 26
    N  = (N - 1) // 26
    seq.append(s)
L = len(seq)

name = ''

for i in range(L):
    name = alph[seq[i]] + name

print(name)