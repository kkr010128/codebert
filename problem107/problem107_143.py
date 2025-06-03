# coding: utf-8
# Your code here!

n=int(input())
x=input()

ones=x.count("1")

a=ones+1
b=ones-1

xda=0
xdb=0
for i in range(n):
    if x[-1-i]=="1":
        xda+=pow(2,i,a)
        xda%=a
        if b==0:
            continue
        xdb+=pow(2,i,b)
        xdb%=b

xds=[-1]*n

for i in range(n):
    if x[-1-i]=="0":
        xds[-1-i]=(xda+pow(2,i,a))%a
    else:
        if b==0:
            continue
        xds[-1-i]=(xdb-pow(2,i,b))%b

    
def popcount(x):
    return bin(x).count("1")
    
def solve(x):
    if x<0:
        return -1
    if x==0:
        return 0
    cnt=0
    while x>0:
        cnt+=1
        x=x%popcount(x)
    return cnt

for xd in xds:
    print(1+solve(xd))

