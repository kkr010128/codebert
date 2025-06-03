K = int(input())
A, B = map(int, input().split())
flag = 0
for n in range(A, B+1):
    if n % K == 0:
        flag = 1
        break
if flag == 0:
    print("NG")
else:
    print("OK")