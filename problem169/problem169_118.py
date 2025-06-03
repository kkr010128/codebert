def main():
    N = int(input())
    A = list(map(int,input().split()))
    buka_num = [0]*(N+1)

    for i in range(N-1):
        buka_num[A[i]] += 1

    for i in range(1,N+1,1):
        print(buka_num[i])

main()
