N = int(input())
a = 0
k = 2*(N-2)+1
for i in range(2,N):
    for j in range(i,N):
        if (i*j<N)and(i!=j):
            a+=2
        elif(i*j<N)and(i==j):
            a+=1
        else:
            break
       
print(a+k)

