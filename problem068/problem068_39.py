str=input()
s=list(str)
q=int(input())
for i in range(q):
    Q=input()
    l=list(Q)
    if 'print' in Q:
        for p in range(6):
            l.pop(0)
        for X in range(len(l)):
            if l[X]==' ':
                x=X
        A=l[0:x]
        a=''.join(A)
        a=int(a)
        B=l[x+1:len(l)]
        b=''.join(B)
        b=int(b)+1
        t=s[a:b]
        str=''.join(t)
        print(str)
    elif 'reverse' in Q:
        for v in range(8):
            l.pop(0)
        for Y in range(len(l)):
            if l[Y]==' ':
                y=Y
        A=l[0:y]
        a=''.join(A)
        a=int(a)
        B=l[y+1:len(l)]
        b=''.join(B)
        b=int(b)+1
        t=s[a:b]
        t.reverse()
        s[a:b]=t
    elif 'replace' in Q:
        for r in range(8):
            l.pop(0)
        for Z in range(len(l)):
            if l[Z]==' ':
                z=Z
                break
        N=0
        while True:
            if l[z+N+1]==' ':
                n=z+N+1
                break
            else:
                N+=1
        A=l[0:z]
        a=''.join(A)
        a=int(a)
        B=l[z+1:n]
        b=''.join(B)
        b=int(b)+1
        t=l[n+1:len(l)]
        s[a:b]=t
