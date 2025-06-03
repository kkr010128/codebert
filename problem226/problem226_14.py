H, N = map(int, input().split())
As = list(map(int, input().split()))

sumA = sum(As)

if sumA >= H:
    print('Yes')
else:
    print('No')
