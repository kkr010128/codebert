X = list(map(int,input().split()))
for i in [0,1]:
    if X.count(X[i]) == 2:
        print('Yes')
        exit()

print('No')
