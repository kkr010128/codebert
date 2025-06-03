N , M = map(int,input().split())
SC = []
for i in range(M):
    SC.append(list(map(int,input().split())))

if M == 0:
    if N == 1:
        print(0)
    else:
        print(10**(N-1))
    exit()
    
if N == 1:
    for i in range(10):
        n = str(i)
        for j in range(M):
            if int(n[SC[j][0]-1]) != SC[j][1]:
                break
            if j == M-1:
                print(i)
                exit()
  
else:
    for i in range(10**(N-1),10**N):
        n = str(i)
        for j in range(M):
            if int(n[SC[j][0]-1]) != SC[j][1]:
                break
            if j == M-1:
                print(i)
                exit()
                
print(-1)