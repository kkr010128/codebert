def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    broken = 0
    cnt = 1
    for i in range(N):
        if cnt == A[i]:
            cnt += 1
        else:
            broken += 1
    print(broken if broken != N else -1)

    

if '__main__' == __name__:
    resolve()
