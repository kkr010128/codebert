N=int(input())
n=len(str(N))
res=0
for a in range(1,N+1):
    a0=str(a)[0]
    a1=str(a)[-1]
    if a0=='0' or a1=='0':
        a_res=res
        continue
    for i in range(1,n+1):
        if i==1:
            if a0==a1:
                res+=1
        elif i==2:
            if 10*int(a1)+int(a0)<=N:
                res+=1
        elif i==n:
            n0=str(N)[0]
            n1=str(N)[-1]
            if n0<a1:
                res+=0
            elif n0>a1:
                res+=10**(i-2)
            else:
                res+=(N-int(a1)*10**(i-1))//10+1
                if n1<a0:
                    res-=1
        else:
            res+=10**(i-2)
print(res)