def goes_to_zero(n):
    cnt = 0
    while(n > 0):
        n %= bin(n).count('1')
        cnt += 1
    return cnt

N = int(input())
X = input()

XC = X.count('1')
XI = int(X, 2)
XCP = XC + 1
XCM = XC - 1
XTP = XI % XCP
XTM = XI % XCM if XCM != 0 else 0

for i in range(N):
    if X[i] == "0":
        print(goes_to_zero((XTP + pow(2, N - 1 - i, XCP)) % XCP) + 1)
    else:
        if XCM == 0:
            print(0)
        else:
            print(goes_to_zero((XTM - pow(2,N - 1 - i, XCM)) % XCM) + 1)