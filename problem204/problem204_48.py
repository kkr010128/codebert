s=input()
n = int(input())
s1=""
s2=""
t=0
for i in range(n):
    m=input().split()
    if len(m)==1:
        t=1-t
    else:
        if t==0:
            if int(m[1])==2:
                s2+=m[2]
            else:
                s1+=m[2]
        else:
            if int(m[1])==2:
                s1+=m[2]
            else:
                s2+=m[2]
    #print(s1,s2)
if t==0:
    s3=s1[::-1]
    print(s3+s+s2)
else:
    s=s[::-1]
    s2=s2[::-1]
    print(s2+s+s1)
            
        
            
