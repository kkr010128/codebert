H1, M1, H2, M2, K = map(int, input().split())

getUpTime = H1 * 60 + M1
goToBed = H2 * 60 + M2

DisposableTime = goToBed - getUpTime
if K > DisposableTime:
    print(0)
else:
    print(DisposableTime - K)