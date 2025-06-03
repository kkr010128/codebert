N = int(input())
A = list(map(int, input().split()))

print(sum([i&1 and a&1 for i,a in enumerate(A,1)]))