n,A,B=map(int,input().split())
z=A+B
if n%z<=A:
    print(int(n/z)*A+n%z)
elif A<=n%z<=z:
    print(int(n/z)*A+A)