import sys
A, B, K = map(int, input().split())

if A >= K:
    A -= K
    print(A, B)
    sys.exit(0)
else:
    K -= A
    if B >= K:
        B -= K
        print(0, B)
        sys.exit(0)
    else:
        print(0, 0)