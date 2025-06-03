A,B,N=map(int,input().split())

i=min(B-1,N)


tmp=(A*i)//B-A*(i//B)

        
print(tmp)