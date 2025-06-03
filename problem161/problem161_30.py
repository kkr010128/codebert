A,B,N = (int(a) for a in input().split())

def f(x) :
    return (A*x)//B - A * (x//B)

if B-1 <= N :
    print(max(f(B-1) , f(N)))
else : 
    print(f(N))

