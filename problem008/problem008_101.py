n=int(input())
a=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    v=list(input().split())
    for j in range(len(v)):
        v[j]=int(v[j])
    x=2
    for k in range(v[1]):
        a[i][v[x+k]-1]=1
#print(a)

stack=[]
v=[]
d=[0]*n
f=[0]*n
t=1

while len(v)<n:
    for i in range(n):
        if i+1 not in v:
            stack.append(i+1)
            d[i]=t
            break
        else: pass
        
    while len(stack)!=0:
        for i in range(n):
            if a[stack[-1]-1][i]==1 and stack[-1]-1!=i and i+1 not in v and i+1 not in stack:
                stack.append(i+1)
                t+=1
                d[i]=t
                break
            elif i==n-1:
                t+=1
                f[stack[-1]-1]=t
                v.append(stack.pop())
            else: pass
            #print("i=",i)
            #print("stack ",stack)
            #print("v ",v)
    t+=1
#print("d=",d," f=",f)
for i in range(n):
    print(i+1,d[i],f[i])

