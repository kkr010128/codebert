n,m=map(int,input().split())
diffs=set()
idxs=set()
i=1
diff=n-1
cnt=0
while 1:
    if i>m:
      break
    while (diff in diffs and n-diff in diffs) or (i+diff in idxs) or (diff==n-diff):
        diff-=1
    diffs.add(n-diff)
    diffs.add(diff)
    idxs.add(i+diff)
    print(i,i+diff)
    i+=1