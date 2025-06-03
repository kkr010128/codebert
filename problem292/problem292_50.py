n = int(input())
d = list(map(int,input().split()))

chofuku = 0
for x in d:
    for y in d:
        chofuku += x*y
chofuku //= 2

nochofuku = 0
for x in d:
    nochofuku += x*x
nochofuku //= 2

print(chofuku-nochofuku)
