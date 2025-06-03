#!/usr/bin/python3


def countpars(s):
    lc = 0
    rc = 0
    for ch in s:
        if ch == '(':
            lc += 1
        else:
            if lc > 0:
                lc -= 1
            else:
                rc += 1
    return (lc, rc)


n = int(input())

ssl = []
ssr = []
for i in range(n):
    (clc, crc) = countpars(input())
    if clc >= crc:
        ssl.append((clc, crc))
    else:
        ssr.append((clc, crc))

ssl.sort(key=lambda x: x[1])
ssr.sort(reverse=True)

lc = 0
rc = 0

for (clc, crc) in ssl:
    lc -= crc
    if lc < 0:
        print('No')
        exit()

    lc += clc

for (clc, crc) in ssr:
    lc -= crc
    if lc < 0:
        print('No')
        exit()
    lc += clc
        

if lc == 0:
    print('Yes')
else:
    print('No')    
    




