a,b=map(int,input().split())
list=[[0 for i in range(2)] for j in range(a)]
for i in range(a):
    list[i]=input().split()
n=0
s=0
while n!=a:
    if int(list[n][1])>b:
        list[n][1]=int(list[n][1])-b
        list.append(list[n])
        list.pop(n)
        s+=b
    else:
        print(list[n][0],s+int(list[n][1]))
        s+=int(list[n][1])
        n+=1

