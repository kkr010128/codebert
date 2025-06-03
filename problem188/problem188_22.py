import numpy as np
inp = input
#fin = open("case_21.txt")
#inp = fin.readline

X, Y, A, B, C = map(int, inp().split())

#red = np.array(list(map(int, inp().split())), np.int32)
#green = np.array(list(map(int, inp().split())), np.int32)
#white = np.array(list(map(int, inp().split())), np.int32)
red = list(map(int, inp().split()))
green = list(map(int, inp().split()))
white = list(map(int, inp().split()))
red.sort(reverse=True)
green.sort(reverse=True)
white.sort(reverse=True)
#fin.close()

#red[::-1].sort()
#green[::-1].sort()
#white[::-1].sort()

idr = 0
idg = 0
idw = 0

total = 0.0
countr = 0
countg = 0
countw = 0
while X > countr and Y > countg and (X+Y > countr+countg+countw):
    if red[idr] >= green[idg]:
        if idw >= C or red[idr] >= white[idw]:
            #eat red
            total += red[idr]
            idr += 1
            countr += 1
        elif idw < C:
            #eat white
            total += white[idw]
            idw += 1
            countw += 1
    else:
        if idw >= C or green[idg] >= white[idw]:
        # eat green
            total += green[idg]
            idg += 1
            countg += 1
        else:
            #eat white
            total += white[idw]
            idw += 1
            countw += 1

#eat remain
if Y <= countg:
    while X > countr+countw:
        # compare red 1st
        if idw < C and red[idr] < white[idw]:
            # eat white
            total += white[idw]
            idw += 1
        else:
            # eat red
            total += red[idr]
            idr += 1
        countr += 1

if X <= countr:
    while Y > countg+countw:
        # compare green 1st
        if idw < C and green[idg] < white[idw]:
            # eat white
            total += white[idw]
            idw += 1
        else:
            # eat green
            total += green[idg]
            idg += 1
        countg += 1

print(int(total))
