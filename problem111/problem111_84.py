def main():
    n = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)

    k = n//2
    if n%2==0:
        print(A[0]+2*sum(A[1:k]))
    else:
        print(A[0]+2*sum(A[1:k])+A[k])
main()