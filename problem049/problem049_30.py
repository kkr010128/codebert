import sys
while 1:
    H,W = map(int,sys.stdin.readline().split())
    if H == W == 0:
        break
    print(('#'*W + '\n')*H)