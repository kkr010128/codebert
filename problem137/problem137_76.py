def main():
    N = int(input())
    A,B = [],[]
    for _ in range(N):
        a,b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 1:
        minMed = A[N//2]
        maxMed = B[N//2]
        print(int(maxMed-minMed)+1)
    else:
        minMed = A[N//2-1] + A[N//2]
        maxMed = B[N//2-1] + B[N//2]
        print(int(maxMed-minMed)+1)

if __name__ == '__main__':
    main()