K = int(input())
A, B = map(int,input().split())

N = B//K
if K*N <A:
    print("NG")
else:
    print("OK")