N, A, B = map(int, input().split())


distance =(B - A - 1 )//2
if( (A % 2 == 0 and B % 2 ==0) or (A%2==1 and B%2==1)):
    ans=(B - A)//2
else:
    ans = min(A-1,N - B) + 1 + distance

print(ans)