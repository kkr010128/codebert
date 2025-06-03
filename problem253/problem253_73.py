n, a, b = map(int, input().split())

if abs(b-a)%2 == 0:
    print(abs(b-a)//2)
else:
    print(min((max(a,b)+min(a,b))//2, (2*n-max(a,b)-min(a,b)+1)//2))