a,b = map(int,input().split())

if a<=b:
    [print(a,end="") for _ in range(b)]
else:
    [print(b,end="") for _ in range(a)]
