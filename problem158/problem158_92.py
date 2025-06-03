K = int(input())
A, B = list(map(int, input().split()))
check = False

for k in range(A, B+1):
    if k % K == 0:
        check = True
    else:
        continue
if check:
    print("OK")
else:
    print("NG")