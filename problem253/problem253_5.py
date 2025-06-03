N,A,B=map(int,input().split())

D=B-A

if D%2:
    a=A-1
    b=N-B
    print(min(a,b)+1+(D-1)//2)
else:
    print(D//2)
