import collections
a=int(input())
b=list(map(int,input().split()))

c=collections.Counter(b)
n,m=zip(*c.most_common())
n,m=list(n),list(m)
o=c.most_common()

result=[0]*a
for i in range(len(o)):
    result[o[i][0]-1]=o[i][1]

for i in result:
    print(i)