N = int(input())
A,B=map(int,input().split())
Na = N
while N <= 1000:
    if A <= N and N <= B:
        print("OK")
        break
    N = N+Na
if N>1000:
    print("NG")