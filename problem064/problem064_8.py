# Ring

ring = input()
word = input()

doubleRing = ring * 2
ringCut = doubleRing.split(word)
# print(ringCut)

if ringCut[0] == doubleRing:
    print('No')
else:
    print('Yes')

