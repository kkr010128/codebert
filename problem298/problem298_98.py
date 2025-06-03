N, K = map(int, input().split())
A = [int(a) for a in input().split()]
print(len([a for a in A if a >= K]))