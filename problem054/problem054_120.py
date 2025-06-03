count = input()
Ss = []
Hs = []
Cs = []
Ds = []
for i in range(int(count)):
    mark, num = input().split()
    if mark is 'S':
        Ss.append(num)
    elif mark is 'H':
        Hs.append(num)
    elif mark is 'C':
        Cs.append(num)
    elif mark is 'D':
        Ds.append(num)

for i in range(1,14):
    if not(str(i) in Ss):
        print("S {0}".format(str(i)))
for i in range(1,14):
    if not(str(i) in Hs):
        print("H {0}".format(str(i)))
for i in range(1,14):
    if not(str(i) in Cs):
        print("C {0}".format(str(i)))
for i in range(1,14):
    if not(str(i) in Ds):
        print("D {0}".format(str(i)))