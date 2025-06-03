H, N = map(int, input().split())
A = [int(x) for x in input().split()]
AA = sum(A)
if AA >= H:
    print("Yes")
else:
    print("No")
