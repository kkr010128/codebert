s=input()
n=len(s)
l=[[0,0] for i in range(n+1)]
ri,le=0,0
for i in range(n):
    l[i][0]=le
    l[-1-i][1]=ri
    if "<"==s[i]:le+=1
    else:le=0
    if ">"==s[-1-i]:
        ri+=1
    else:ri=0

l[n][0]=le
l[0][1]=ri
print(sum(max(a,s) for a,s in l))