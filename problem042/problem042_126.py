import sys
i=1
while True:
    x=sys.stdin.readline().strip()
    if x=="0":
        break;
    print("Case %d: %s"%(i,x))
    i+=1