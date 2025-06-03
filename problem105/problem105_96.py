N = int(input())
A = [int(i) for i in input().split()]
print(sum(a % 2 for a in A[::2]))
