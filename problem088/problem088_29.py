N=int(input())
A=str(input())


def ans176(N:int, A:str):
    A=list(map(int,A.split()))
    step_count=0
    max=A[0]
    for i in range(1,N):
        if A[i]<max:
            step_count=step_count+max-A[i]
        else:
            max=A[i]
    return(step_count)

print(ans176(N,A))