import sys
def input():
    return sys.stdin.readline()[:-1]
t=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
at1=a[0]*t[0]
at2=a[1]*t[1]
bt1=b[0]*t[0]
bt2=b[1]*t[1]
if at1+at2==bt1+bt2:
    print("infinity")
    quit()

if at1>bt1:
    if at1+at2>bt1+bt2:
        print(0)
        quit()
    sa1=at1-bt1
    sa2=bt1+bt2-at1-at2
    # print(sa1//sa2*2+1)
else:
    if bt1+bt2>at1+at2:
        print(0)
        quit()
    sa1=bt1-at1
    sa2=-(bt1+bt2-at1-at2)
    # print(sa1//sa2*2+1)
if sa1%sa2==0:
    print(sa1//sa2*2)
else:
    print(sa1//sa2*2+1)