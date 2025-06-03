n,m=map(int,input().split())
li=[]
if n==1:
    score="0"
else:
    score="1"+"0"*(n-1)
for i in range(m):
    s,c=map(int,input().split())
    if n!=1 and (s,c)==(1,0):
        print("-1")
        quit()
    li.append([s,c])
    for j in range(len(li)):
        if li[j][0]==s and li[j][1]!=c:
            print("-1")
            quit()
    score=score[:s-1]+str(c)+score[s:]
print(int(score))
