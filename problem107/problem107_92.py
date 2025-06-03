N = int(input())
X = list(input())
X = [int(x) for x in X]
popcnt = 0
for i in range(N):
    if X[i]:
        popcnt += 1

Ys = [0,0]
for i in range(N):
    if X[i]:
        Ys[0] += pow(2,N-1-i,popcnt+1)
        Ys[0] %= popcnt+1

if popcnt > 1:
    for i in range(N):
        if X[i]:
            Ys[1] += pow(2,N-1-i,popcnt-1)
            Ys[1] %= popcnt-1


for i in range(N):
    if X[i]:#1->0
        mod = popcnt-1
        if mod == 0:
            print(0)
            continue
        Y = Ys[1] - pow(2,N-1-i,mod)
    else:#0->1
        mod = popcnt+1
        Y = Ys[0] + pow(2,N-1-i,mod)
	
    Y %= mod
    ans = 1

    if Y == 0:
        print(ans)
        continue
        
    while Y > 0:
        L = Y.bit_length()
        mod = 0
        for j in range(L):
            if Y>>j&1:
                mod += 1
        Y %= mod
        ans += 1
    print(ans)