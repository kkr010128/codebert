N = int(input())
X = str(input())
X10 = int(X,2)

one_num = X.count("1")
X10_pl = X10%(one_num+1)
if one_num>1:
    X10_mi = X10%(one_num-1)
else:
    X10_mi = 0

for i in range(N):
    target = int(X[i])
    
    if target == 0:
        ones = one_num + 1
        plus = pow(2,N-i-1,ones)
        Xnow = (X10_pl + plus)%ones
        
    else:
        if one_num == 1:
            print(0)
            continue
        ones = one_num-1
        plus = -pow(2,N-i-1,ones)
        Xnow = (X10_mi + plus)%ones

    count=1
    
    while Xnow > 0:
        Xnow2 = bin(Xnow)
        ones = Xnow2.count("1")
        Xnow = Xnow%ones
        count+=1
        
    print(count)

