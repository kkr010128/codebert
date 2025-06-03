l=map(str,raw_input().split())
chk=[]
op='-+*'
while len(l):
    k=l.pop(0)
    if k in op:
        b=chk.pop()
        a=chk.pop()
        chk.append(str(eval(a+k+b)))
    else:
        chk.append(k)
print chk[0]