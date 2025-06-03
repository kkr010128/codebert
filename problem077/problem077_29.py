a,b,c,d=map(int,input().split())
A=a*c
B=a*d
C=b*c
D=b*d
N=[A,B,C,D]
print(max(N))