N=int(input())
A=list(map(int,input().split()))
 
mul=1
if 0 in A:print("0")
else:
    for i in range(N):
        mul*=A[i]
        if mul>pow(10,18):
            print("-1")
            break
        elif i==N-1:print(mul)