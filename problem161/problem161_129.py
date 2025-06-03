def resolve():
    A, B, N = map(int, input().split())
    if B <= N+1:
        print(A*(B-1)//B)
    else:
        print(A*N//B)
resolve()