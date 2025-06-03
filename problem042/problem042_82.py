import sys
cnt = 1
while 1:
    x=sys.stdin.readline().strip()
    if x == '0':
        break;
    print("Case " + str(cnt) + ": " + x)
    cnt+=1