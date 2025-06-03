from collections import defaultdict as d
n=int(input())
a=list(map(int,input().split()))
p=d(int)
l=0
for i in a:
    p[i]+=1
    l+=i
for i in range(int(input())):
    b,c=map(int,input().split())
    l+=p[b]*(c-b)
    p[c]+=p[b]
    p[b]=0
    print(l)