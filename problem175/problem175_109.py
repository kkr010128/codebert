import sys
import math
import bisect
from collections import defaultdict,deque

# input = sys.stdin.readline
def inar():
    return [int(el) for el in input().split()]
# def find(a,b,c):
#     gc=math.gcd(a,b)
#     return math.gcd(gc,c)
def main():
    n=int(input())
    string=input()
    r=[]
    g=[]
    b=[]
    for i in range(n):
        if string[i]=="R":
            r.append(i)
        elif string[i]=="G":
            g.append(i)
        else:
            b.append(i)
    ans=0
    r.sort()
    g.sort()
    b.sort()
    # print(r)
    # print(g)
    # print(b)
    # print(len(b))
    # ans1=0
    # fir=[]
    # for i in range(len(r)):
    #     for j in range(len(g)):
    #         for k in range(len(b)):
    #             ls=[r[i],g[j],b[k]]
    #             ls.sort()
    #             if ls[1]-ls[0]!=ls[2]-ls[1]:
    #                 ans1+=1
    #         fir.append(ans1)
    # # print(ans1)

    # print("-------------------check---------------")
    # are=[]
    for i in range(len(r)):
        for j in range(len(g)):
            ans+=len(b)
            chota=min(g[j],r[i])
            bada=max(g[j],r[i])
            diff=bada-chota

            left=bisect.bisect_left(b,bada+diff)
            right=bisect.bisect_left(b,chota-diff)

            lol=(bada+chota)
            if lol%2==0:
                beech=lol//2
                ind=bisect.bisect_left(b,beech)
                if ind<len(b) and b[ind]==beech:
                    ans-=1
            if (left<len(b) and b[left]==bada+diff):
                ans-=1
            if (right<len(b) and b[right]==chota-diff):
                ans-=1

            # are.append(ans)
    print(ans)
    # for i in range(len(are)):
    #     print(are[i],fir[i])


if __name__ == '__main__':
    main()



