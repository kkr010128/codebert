def solve(N):
    if N%2==1:
        return 0
    N2=(N-N%10)//10
    count_zero=N2
    x=5
    while N2>=x:
        count_zero+=N2//x
        x*=5
    return count_zero
    
        
    

N=int(input())
print(solve(N))