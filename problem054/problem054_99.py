n = int(input())
S = []
H = []
C = []
D = []

for x in range(0,n):
    L = raw_input().split()
    if L[0] == "S": S.append(int(L[1]))
    elif L[0] == "H": H.append(int(L[1]))
    elif L[0] == "C": C.append(int(L[1]))
    else: D.append(int(L[1]))

for x in range(1,14):
    if not x in S: print "S {}".format(x)
for x in range(1,14):
    if not x in H: print "H {}".format(x)
for x in range(1,14):
    if not x in C: print "C {}".format(x)
for x in range(1,14):
    if not x in D: print "D {}".format(x)