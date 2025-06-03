import sys
input=sys.stdin.readline
n=int(input())
x=input().rstrip()
x10=int(x,2)
pcx=x.count("1")

plus=x10%(pcx+1)
if pcx>=2:
    minus=x10%(pcx-1)

def popcnt(x):
    cnt=1
    while x>=1:
        x%=(bin(x).count("1"))
        cnt+=1
    return cnt

for i in range(n):
    if x[i]=="0":
        amari=(plus+pow(2,n-i-1,pcx+1))%(pcx+1)
        print(popcnt(amari))
    else:
        if pcx==1:
            print(0)
        else:
            amari=(minus-pow(2,n-i-1,pcx-1))%(pcx-1)
            print(popcnt(amari))