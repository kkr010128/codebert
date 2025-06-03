A = list(map(int , input().split()))
B = list(map(int , input().split()))
print(sum(sorted(B)[:A[1]]))