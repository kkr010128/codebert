def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil,pi,factorial
    from operator import itemgetter
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    def LI2(): return [int(input()) for i in range(n)]
    def MXI(): return [[LI()]for i in range(n)]
    def SI(): return input().rstrip()
    def printns(x): print('\n'.join(x))
    def printni(x): print('\n'.join(list(map(str,x))))
    inf = 10**17
    mod = 10**9+7
#main code here!
    h,w,k=MI()
    cake=[SI() for i in range(h)]
    last=[-1 for i in range(w)]
    for i in range(w):
        for j in range(h):
            if cake[j][i]=="#":
                last[i]=j
    lis=[[0]*w  for i in range(h)]
    ans=0
    for i in range(w):  
        if last[i]==-1:
            continue
        if last[i]!=-1:
            ans+=1
        for j in range(h):
            lis[j][i]=ans
            if cake[j][i]=="#":
                if last[i]!=j:
                    ans+=1
    #print(lis)
    pos=[]
    for i in range(w):
        if last[i]!=-1:
            pos.append(i)
    pos.append(w)
    for i in range(w):
        if last[i]==-1:
            u=pos[bisect_left(pos,i)]
            #print(u)
            if u!=w:
                for j in range(h):
                    lis[j][i]=lis[j][u]
            else:
                for j in range(h):
                    lis[j][i]=lis[j][pos[-2]]

            
        
    
    for i in range(h):
        print(*lis[i])
    #print(lis)

            
            
            

    
        
        
        
        
    
        
                    
            
        



        
        
        
        
        
    
if __name__=="__main__":
    main()

