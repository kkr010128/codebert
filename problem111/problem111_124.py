def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse = True)
    ans = A[0]
    kazu = (N-2)//2
    amari = (N-2)%2
    for i in range(1,kazu+1,1):
        #print(i)
        ans += (A[i]*2)

    if amari==1:
        ans += A[i+1]*amari

    print(ans)

main()
