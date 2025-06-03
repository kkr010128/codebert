a,b,c = map(int,input().split())

K = int(input())

judge = False
for i in range(K+1):
    for j in range(K+1):
        for k in range(K+1):
            x = a*2**i
            y = b*2**j
            z = c*2**k
            if i+j+k <= K and x < y and y < z:
                judge = True
                
if judge:
    print("Yes")
else:
    print("No")