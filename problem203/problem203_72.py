import sys
A, B = map(int, input().split())
ans = -1
for x in range(1010):
    a = int((x*0.08))
    b = int(x*0.1)
    if a == A and b == B:
        print(x)
        sys.exit()
print(ans)