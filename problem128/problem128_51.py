X,N = map(int,input().split())
p = list(map(int,input().split()))
diff = 1
if(X not in p):
    print(X)
    exit()
while(diff < 200):
    if(X-diff not in p):
        print(X-diff)
        exit()
    elif(X+diff not in p):
        print(X+diff)
        exit()
    diff += 1