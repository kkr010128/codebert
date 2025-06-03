K = int(input())
A, B = list(map(int, input().split()))

i = 1
flag = False
while K * i <= B:
    if K * i >= A:
        flag = True
    i += 1

if flag:
    print("OK")
else:
    print("NG")
