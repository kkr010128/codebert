import sys
input=sys.stdin.readline
N=int(input())
S=input()
Q=int(input())
D={}
A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(26):
    D[A[i]]=i
n=1
while n<N:
    n*=2

seg=[0 for i in range(n*2)]
#print(seg)

for i in range(N):
    seg[n-1+i]=1<<D[S[i]]
    k=n-1+i
    while k>0:
        k=(k-1)//2
        seg[k]=(seg[k*2+1]|seg[k*2+2])
#print(list(bin(seg[0])).count("1"))

#0indexでa番目の値をbに変更
def update(a,b):
    a+=n-1
    seg[a]=1<<D[b]
    while a>0:
        a=(a-1)//2
        seg[a]=(seg[a*2+1]|seg[a*2+2])

#print(seg)

#A～B-1(0-index)までの累積和を求める
#1～2までの累積和なら(1,3,0,0,n)
#Kは接点番号？L,Rはその接点が[L,R)に対応づいていることを表す？
#外部からはquery(A,B,0,0,n)として呼び出す
def query(A,B,K,L,R):
    if K>=len(seg):
        return 0
    if R<=A or B<=L:
        return 0
    elif A<=L and R<=B:
        return seg[K]
    else:
        vl=query(A,B,K*2+1,L,(L+R)//2)
        vr=query(A,B,K*2+2,(L+R)//2,R)
        #print(vl,vr)
        return vl|vr
#print(n,len(seg))
#print("P",query(2,4,0,0,n),len(query(2,4,0,0,n)))
#update(3,"a")
#print(seg)
#print(query(2,4,0,0,n))
for i in range(Q):
    x,y,z=list(input().split())
    if x=="1":
        update(int(y)-1,z)
    else:
        print(list(bin(query(int(y)-1,int(z),0,0,n))).count("1"))
