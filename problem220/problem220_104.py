S,T=list(input().split())
A,B=list(map(int,input().split()))
U=input()
D={}
D[S]=A
D[T]=B
D[U]-=1
print(D[S],D[T])