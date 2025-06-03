N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
c=0
b=0
for i in range(M):
    b+=B[i]
    if b<=K:
        c+=1
    else:
        break
a=0
b=sum(B)
j=M
ans=0
for i in range(N):
    a+=A[i]
    if a>K:
        break
    while a+b>K:
        b-=B[-1]
        B.pop(-1)
        j-=1
    ans=max(ans,i+j+1)
ans=max(ans,c)
print(ans)






    

        




    















    



    





    






        






    
















        


























            
    


    


    
    














    


    












