import sys
X,K,D= map(int,input().split())
temp = X

if abs(X) > K*D:
    print(abs(X)-K*D)
    sys.exit()
    
for t in range(K):
    # 絶対値の小さい方に移動
    if abs(temp - D) < abs(temp + D):
        temp = temp-D
    else:
        temp = temp+D

    # 移動幅より小さくなったとき
    if abs(temp) < D:
        if (K-t-1) % 2 == 0:
            print(abs(temp))
            sys.exit()
        else:
            if abs(temp - D) < abs(temp + D):
                temp = temp-D
                print(abs(temp))
                sys.exit()
            else:
                temp = temp+D
                print(abs(temp))
                sys.exit()

print(abs(temp))

