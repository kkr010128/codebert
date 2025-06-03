a,b=map(int,input().split())

if a>b:
    if a%b==0:
        gcd=b
    else:
        p=a
        q=b
        r=p%q
        while r!=0:
            p=q
            q=r
            r=p%q
            if r==0:
            	gcd=q
            	break
elif a<b:
    if b%a==0:
    	gcd=a
    else:
        p=b
        q=a
        r=p%q
        while r!=0:
            p=q
            q=r
            r=p%q
            if r==0:
            	gcd=q
            	break
A=a//gcd
B=b//gcd
print(A*B*gcd)