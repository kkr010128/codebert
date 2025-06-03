def main():
    n = int(input())
    A = [0]*n
    B = [0]*n
    for i in range(n):
        a,b = map(int,input().split())
        A[i] = a
        B[i] = b
    A.sort()
    B.sort()
    if n%2 == 0:
        m1 = (A[n//2-1]+A[n//2])/2
        m2 = (B[n//2-1]+B[n//2])/2
        print(int(2*(m2-m1))+1)
    else:
        print(B[(n+1)//2-1]-A[(n+1)//2-1]+1)    
main()