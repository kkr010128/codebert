N,M = map(int,input().split())

a = [False]*(N+1)
b = [0]*(N+1)



for i in range(M):
    c = input().split()
    if c[1] == "AC":
        a[int(c[0])] = True
    elif c[1] == "WA" and a[int(c[0])] == False:
        b[int(c[0])] += 1
            

for j in range(N+1):
    if a[j] == False:
        b[j] = 0
        
print(sum(a),sum(b))