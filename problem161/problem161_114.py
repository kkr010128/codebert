A,B,N = map(int,input().split())

if N < B:
    x = N
    ans = (A*x/B)//1
else:
    x = B - 1
    ans = (A*x/B)//1

print(int(ans))