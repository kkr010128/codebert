def popcount(x):
    return bin(x).count("1")


n=int(input())
x=input()
num=int(x,2)
cnt=popcount(num)

A=[]
for i in range(n):
    number=num
    if x[i]=="1" and cnt==1:A.append(-1)
    elif x[i]=="1":
        number %=cnt-1
        A.append((number-pow(2,n-i-1,cnt-1))%(cnt-1))
    else:
        number %=cnt+1
        A.append((number+pow(2,n-i-1,cnt+1))%(cnt+1))

for i in A:
    ans=i
    if ans==-1:print(0)
    else:
        point=1
        while ans!=0:
            ans %=popcount(ans)
            point +=1
        print(point)