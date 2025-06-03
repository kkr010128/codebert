N,K = map(int,input().split())
counter = 0

for k in range(K,N+2): 
    counter += k*(N-k+1) + 1


print(counter%(pow(10,9)+7))