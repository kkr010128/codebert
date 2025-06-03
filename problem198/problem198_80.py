from collections import deque
N=int(input())
d=deque()
d.append("a")
dall=deque()
dall.append(d)
i=0
while i<N-1:
    length=len(dall)
    j=0
    while j<length:
        l=dall.popleft()
        llen=len(set(l))
        for k in range(llen+1):
            q = deque()
            for m in range(len(l)):
                c = l.popleft()
                q.append(c)
                l.append(c)
            q.append(chr(ord("a")+k))
            dall.append(q)
        #print(dall)
        #input()
        j=j+1
    i=i+1
    #print(dall)
    #input()
#print(len(dall))
ans=[]
for i in range(len(dall)):
    ans.append("".join(dall[i]))
ans.sort()
for i in range(len(ans)):
    print(ans[i])