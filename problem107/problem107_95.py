n=int(input())
x=input()
p=x.count('1')

#愚直に解く関数を定義
def solve(n):
    count=0
    while n:
        popcount=bin(n).count('1')
        n%=popcount
        count+=1
    return count+1

#popcount(x)が0,1だった場合に対応
if p==0:
    for i in range(n):
        print(1)
    exit()
elif p==1:
    z=x.index('1')
    t=pow(2,n-z-1,p+1)
    for i in range(n):
        if i==z:
            print(0)
        else:
            tmp=(t+pow(2,n-i-1,p+1))%(p+1)
            print(solve(tmp))
    exit()


#2^i mod(p+1),2^i mod(p-1)のリストを作成
a,b=[],[]
for i in range(n):
    a.append(pow(2,i,p+1))
    b.append(pow(2,i,p-1))

#x mod(p+1),x mod(p-1)を計算
a1,b1=0,0
for i in range(n):
    if x[-1-i]=='1':
        a1+=a[i]
        b1+=b[i]

#本計算
for i in range(n):
    if x[i]=='1':
        tmp=(b1-b[-1-i])%(p-1)
    else:
        tmp=(a1+a[-1-i])%(p+1)
    print(solve(tmp))