x,y,a,b,c=map(int,input().split())
plist=list(map(int,input().split()))
qlist=list(map(int,input().split()))
rlist=list(map(int,input().split()))

plist.sort()
qlist.sort()
rlist.sort(reverse=True)


pgensen=plist[a-x:]
qgensen=qlist[b-y:]

tmplist=pgensen+qgensen
tmplist.sort()

replacesum=0
for i in range(min(x+y,len(rlist))):
    if tmplist[i] >= rlist[i]:
        break
    else:
        replacesum+=rlist[i]-tmplist[i]

print(sum(tmplist)+replacesum)
