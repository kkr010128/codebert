s=input()
stack=[]
tmpans=[]
ans=[]
for k,v in enumerate(s):
    if v=="\\":
        stack.append(k)
    elif v=="/" and len(stack)>0:
        p=stack.pop()
        a=k-p
        while len(tmpans)>0 and tmpans[-1][-1]>p:
            a+=tmpans[-1][0]
            tmpans.pop()
        tmpans.append([a,p])
x=[i[0] for i in tmpans]
print(sum(x))
print(len(x),*x)
