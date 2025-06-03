n=int(input())
s=input()
ans=0

def my_index(l,x,default=-1):
    if x in l:
        return l.index(x)
    else:
        return default

for i in range(10**3):
    i=str(i).zfill(3)
    if my_index(s,i[0])!=-1:
        s2=s[my_index(s,i[0])+1:]
        if my_index(s2,i[1])!=-1:
            s3=s2[my_index(s2,i[1])+1:]
            if my_index(s3,i[2])!=-1:
                ans+=1
print(ans)

