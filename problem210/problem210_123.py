import sys
import math
import bisect
def input():
    return sys.stdin.readline()[:-1]

n=int(input())
s=list(input())
q=int(input())
ans=[]
dic = {}

for i in range(97,97+26):
    dic[chr(i)]=[]

for num,i in enumerate(s):
    dic[i].append(num)

for i in range(q):
    num,l,r = map(str,input().split())
    if int(num)==1:
        l=int(l)-1
        if s[l] == r:
            continue
        else:
            dic[s[l]].pop(bisect.bisect_left(dic[s[l]],l))
            bisect.insort_left(dic[r],l)
            s[l] = r
    else:
        cnt=0
        l=int(l)
        r=int(r)
        for li in dic.values():
            ind = bisect.bisect_left(li,l-1)
            if ind>=len(li):continue
            if li[ind]<=r-1:
                cnt+=1
        ans.append(cnt)

print(*ans,sep="\n")
