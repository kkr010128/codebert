A,B=map(int,input().split())
ma,mi=0,0
ma=max(A,B)
mi=min(A,B)

if A%B==0 or B%A==0:
    print(ma)

else :
    for i in range(2,ma+1):
        if (ma*i)%mi==0:
            print(ma*i)
            break
        i+=(mi-1)
