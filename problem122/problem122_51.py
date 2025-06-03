N=int(input())
A=list(map(int,input().split()))
Q=int(input())
S=[list(map(int,input().split())) for i in range(Q)]

l=[0]*10**6
total=0

for i in range(N) :
    l[A[i]]+=1   #各数字の個数
    total+=A[i]  #初期総和

for i in range(Q) :
    s0=S[i][0]  #Bの値、交換した値
    s1=S[i][1]  #Cの値、交換する値
    total+=s1*l[s0]-s0*l[s0]
    l[s1]+=l[s0]
    l[s0]=0
    print(total)