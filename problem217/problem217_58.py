N = int(input())
A = list(map(int, input().split()))
is_approved = True
for i in range(N):
    if A[i] % 2 != 0:
        continue
    if A[i] % 3 != 0 and A[i] % 5 != 0:
        is_approved = False
        break
if is_approved:
    print("APPROVED")
else:
    print("DENIED")