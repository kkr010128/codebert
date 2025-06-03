N, A, B = map(int, input().split())

mid = (B - A)//2
left = ((A-1+B-1)+1)//2
right = ((N-B+N-A)+1)//2

if (B - A)%2==0:
    print(mid)
else:
    print(min(left, right))