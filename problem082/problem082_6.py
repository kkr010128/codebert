# import math
# import statistics
a=input()
b=input()
#b,c=int(input()),int(input())
c,d=[],[]
for i in a:
    c.append(i)
for i in b:
    d.append(i)
#e1,e2 = map(int,input().split())
# f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
ma=[]
if b in a:
    print(0)
else:
    for i in range(len(c)-len(d)+1):
        count=0
        for k in range(len(d)):
            if c[i:len(d)+i][k]!=d[k]:
                count+=1
        ma.append(count)
    print(min(ma))