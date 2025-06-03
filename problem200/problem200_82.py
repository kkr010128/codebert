_, _, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
xyc = [tuple(map(int, input().split())) for i in range(M)]
print(min([min(A)+min(B)]+[A[x-1]+B[y-1]-c for x, y, c in xyc]))
