H, N = [int(v) for v in input().rstrip().split()]
A = [int(v) for v in input().rstrip().split()]
total = sum(A)
r = 'Yes' if H <= total else 'No'
print(r)
