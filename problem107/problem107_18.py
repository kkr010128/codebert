N = int(input())
X = input()

def popcount(x):
    tmp = x
    count = 0
    while tmp > 0:
        if tmp & 1 == 1:
            count += 1
        tmp >>= 1
    
    return count

x = int(X, 2)
pcx = X.count("1")
pc1 = x % (pcx - 1) if pcx > 1 else 0
pc2 = x % (pcx + 1)


for i in range(N):
    if X[i] == '0':
        X_next = pc2 + pow(2,N-1-i,pcx+1)
        X_pop_next = pcx + 1
    elif X[i] == '1' and pcx - 1 != 0:
        X_next = pc1 - pow(2,N-1-i,pcx-1)
        X_pop_next = pcx - 1
    else :
        print(0)
        continue
    
        
    if X_pop_next == 0:
        print(0)
        continue
        
    X_next = X_next % X_pop_next
    ans = 1
    
    while X_next != 0:
        X_next = X_next % popcount(X_next)
        ans += 1
    
    print(ans)