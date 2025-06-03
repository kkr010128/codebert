def main() :
    N,K=map(int,input().split())              #N個の整数,K個の積
    A=list(map(int,input().split()))
    mod=10**9+7
    
    minusA=sorted([i for i in A if i < 0], reverse=True) #負で絶対値が小さい数字順
    plusA=sorted([i for i in A if i >= 0])               #正で絶対値が小さい数字順
 
    start=1
    if len(plusA)==0 and K%2==1 :        #負の整数のみ,Kの個数は奇数
        for i in minusA[:K] :
            start=start*i%mod
        print(start)
        exit()

    while K>0 :
        if K== 1 or len(minusA)<=1 :     #Kの個数が1個のとき、または負の整数が1個以下のとき
            if len(plusA)==0 :           #正の整数が存在しない場合
                start*=minusA.pop()
            elif len(plusA)>0 :          #正の整数が存在する場合
                start*=plusA.pop()
            K-=1                         #この場合、Kを1個減らしていってループさせている

        elif len(plusA)<= 1 :            #正の整数が1個以下のとき
            start*=minusA.pop()*minusA.pop()
            K-=2

        elif plusA[-1]*plusA[-2]>minusA[-1]*minusA[-2] :
            start*=plusA.pop()
            K-=1

        elif plusA[-1]*plusA[-2]<=minusA[-1]*minusA[-2] :
            start*=minusA.pop()*minusA.pop()
            K-=2

        start%=mod
    else :
        print(start)



if __name__=="__main__" :
    main()