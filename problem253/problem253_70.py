N,A,B = map(int,input().split())

if (B-A)%2 == 0:
    ans = [N-A,(B-A)//2,B-1]
    print(min(ans))
else:
    ans = [N-A,B-1,((B-A-1)//2)+(N-B+1),((B-A-1)//2)+A]
    print(min(ans))