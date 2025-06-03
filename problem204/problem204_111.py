#

import sys
input=sys.stdin.readline

def main():
    S=input().strip("\n")
    Q=int(input())
    sign=True
    head=[]
    tail=[]
    for i in range(Q):
        q=tuple(input().split())
        if q[0]=="1":
            sign^=True
        else:
            if (q[1]=="1" and sign==True) or (q[1]=="2" and sign==False):
                head.append(q[2])
            else:
                tail.append(q[2])
    if sign==True:
        print("".join(head[::-1])+S+"".join(tail))
    else:
        print("".join(tail[::-1])+S[::-1]+"".join(head))
    
if __name__=="__main__":
    main()
