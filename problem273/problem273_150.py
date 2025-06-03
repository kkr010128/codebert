# -*- coding: utf-8 -*-
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
write = sys.stdout.write
# template


def solve():
    n,k=map(int, readline().split())
    a = list(map(int, readline().split()))
    b=[0]*(n+1)

    for i in range(n):
        b[i+1]=b[i]+a[i]-1
        b[i+1]%=k
    count=0
    from collections import defaultdict
    dp=defaultdict(list)
    for i in range(n+1):
        dp[b[i]].append(i)
    #print(dp,b)
    for item in dp:
        #print(count)
        if len(dp[item])<2:
            continue
        l=0
        r=1
        li=dp[item]
        while(l<len(li)):
            if l==r:
                r+=1
                continue
            if r<len(li) and li[r]-li[l]<k:
                r+=1
            else:
                count+=r-l-1
                l+=1
    print(count)

        
'''
    for i in range(k):
        if dp[i]<2:
            continue
        count+=dp[i]*(dp[i]-1)//2
'''
    


if __name__ == "__main__":
    solve()