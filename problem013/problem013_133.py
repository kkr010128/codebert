n=int(raw_input().strip())
lst=[]
minval=0x3f3f3f3f
ans=-0x3f3f3f3f
for i in xrange(n):
    val=int(raw_input().strip())
    if(i>=1):
        #print val,minval
        ans=max(ans,val-minval)
    minval = min(minval, val)
print ans

