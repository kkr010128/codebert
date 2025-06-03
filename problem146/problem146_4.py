from sys import stdin
from math import gcd
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=[0]*n
    b=[0]*n
    for i in range(n):
        a[i],b[i]=map(int,readline().split())

    mod=1000000007
    d=dict()
    d[(1,0)]=[0,0]
    ans=1
    zeros=0
    for i in range(n):
        up=a[i]
        down=b[i]
        if up==0 and down==0:
            zeros+=1
        else:
            g=gcd(up,down)
            up//=g
            down//=g
            if up==0:
                down=1
            elif down==0:
                up==1
            elif down<0:
                down*=-1
                up*=-1

            if up==1 and down==0:
                d[(1,0)][0]+=1
            elif up==0 and down==1:
                d[(1,0)][1]+=1
            elif up>0:
                if (up,down) not in d and (-down,up) not in d:
                    d[(up,down)]=[1,0]
                elif (up,down) in d:
                    d[(up,down)][0]+=1
                else:
                    d[(-down,up)][1]+=1
            elif up<0:
                if (up,down) not in d and (down,-up) not in d:
                    d[(up,down)]=[1,0]
                elif (up,down) in d:
                    d[(up,down)][0]+=1
                else:
                    d[(down,-up)][1]+=1

    for v in d.values():
        ans*=pow(2,v[0])+pow(2,v[1])-1
        ans%=mod
    ans-=1
    ans+=zeros
    ans%=mod
    print(ans)
    
if __name__=="__main__":
    main()