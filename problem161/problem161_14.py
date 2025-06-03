A, B, N = map(int, input().split())
x = N if B-1 > N else B-1
print(A*x//B-A*(x//B))