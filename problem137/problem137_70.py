def main():
    n = int(input())
    A,B = [],[]
    for i in range(n):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    if n%2==1:
        a_ = sorted(A)[(n-1)//2]
        b_ = sorted(B)[(n-1)//2]
        print(b_-a_+1)
    else:
        A,B = sorted(A),sorted(B)
        a_ = (A[n//2]+A[n//2-1])/2
        b_ = (B[n//2]+B[n//2-1])/2
        print(int(2*(b_-a_))+1)
    
if __name__ == "__main__":
    main()
