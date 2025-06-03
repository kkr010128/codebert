try:
    
    while True:
        N=list(str(input()))
        
        M=int(input())
    
        for i in range(M):
            H=int(input())
            for j in range(H):
                A=N[0]
                N.remove(A)
                N.append(A)
                j+=1
            
        for k in range(len(N)):  
            print(N[k],end='')
        
        print()
        
except EOFError:
    pass
