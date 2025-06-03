def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    cnt = 0

    for i in range(M):
        cnt += A[i]

    if  N < cnt:
        return -1
    else:
        return N - cnt

print(main())
