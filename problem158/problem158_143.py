K = int(input())
A, B = map(int, input().split())

i = A
while (i % K != 0) and (i <= B):
    i += 1

if i == B+1:
    print("NG")
else:
    print("OK")