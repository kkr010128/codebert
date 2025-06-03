import collections
N=int(input())
A=list(input().split())
a=collections.Counter(A)
A=[int(i) for i in A]
S=sum(A)
Q=int(input())
for i in range(Q):
    B,C=input().split()
    if B in a:
        b=a[B]
        S-=int(B)*b
        S+=int(C)*b
        del a[B]
        if C in a:
            a[C]+=b
        else:
            a[C]=b
    print(S)







    



    





    






        






    
















        


























            
    


    


    
    














    


    












