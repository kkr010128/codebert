def solve(m, A):
    if A[0] == m: return True
    if len(A)==1: return False
    if m < A[0] : return solve(m, A[1:])
    if solve(m-A[0], A[1:]):
        return True
    return solve(m, A[1:])

if __name__=='__main__':
    n=int(input()) 
    A=list(map(int,input().split()))
    q=int(input()) 
    Q=list(map(int,input().split()))
    for m in Q:
        if   m > sum(A): print('no')
        elif solve(m,A): print('yes') 
        else           : print('no') 