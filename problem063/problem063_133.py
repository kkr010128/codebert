import sys

az = [0 for i in range(26)]
s = sys.stdin.read().lower()
l = [ord(i) for i in s]

for i in range(len(l)):
    c = l[i] - 97
    if(c >= 0 and c <= 26):
        az[c] += 1

for i in range(26):
    print('{} : {}'.format(chr(i + 97),az[i]))