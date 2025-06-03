import numpy as np

H,W,K = list(map(int, input().split()))
t=[]
for i in range(H):
    t.append([int(i) for i in input().replace(".","0").replace("#","1")])

cnt = 0
for i in range(2**H):
    for j in range(2**W):
        d = np.array(t)
        i_2 = [int(k) for k in bin(i)[2:].rjust(H,"0")]
        j_2 = [ int(k) for k in bin(j)[2:].rjust(W,"0")]
        #print(i_2)
        #print(j_2)
        
        d= ((d.T)*i_2).T
        d= d*j_2
        
        num = d.sum()
        if num == K:
            cnt +=1
            
print(cnt)