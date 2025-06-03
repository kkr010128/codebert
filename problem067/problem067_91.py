import sys
lines = [line.split() for line in sys.stdin]
T = H = 0
n = int(lines[0][0])
for w1,w2 in lines[1:]:
    if w1 > w2:
        T += 3
    elif w1 < w2:
        H += 3
    else:
        T += 1
        H += 1
print (str(T) + " " + str(H))