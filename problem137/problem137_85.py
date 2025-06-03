N = int(input())
left = []
right = []
for _ in range(N):
    l, r = map(int, input().split())
    left.append(l)
    right.append(r)
left.sort()
right.sort()
if N%2==0:
    for i, (l, r) in enumerate(zip(left, right), 1):
        if i==N//2:
            L = l
            R = r
        if i==N//2+1:
            R +=r
            L += l
            print((R-L)+1)
else:
    for i, (l, r) in enumerate(zip(left, right), 1):
        if i==N//2+1:
            print(r-l+1)