s=input()
ans=0
if s=="SSS":
    ans=0
if s=="SSR" or s=="SRS" or s=="RSS" or s=="RSR":
    ans=1
if s=="RRS" or s=="SRR":
    ans=2
if s=="RRR":
    ans=3

print(ans)