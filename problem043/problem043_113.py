import sys

for i,ws in enumerate(sys.stdin,1):
    list = sorted(map(int, ws[:-1].split()))

    if list[0] == 0 and list[1] == 0:
        break

    print(' '.join(map(str,list)))