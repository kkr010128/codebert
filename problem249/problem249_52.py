A, B, K = map(int, input().split())

if A-K >= 0:
    print(A-K, B)
else:
    if  B-(K-A)<0:
        print(0, 0)
        quit()
    print(0, B-(K-A))