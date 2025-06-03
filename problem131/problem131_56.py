A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if A > B:
    x = A
    A = B
    B = x

nowA = A+T*V
nowB = B+T*W
if nowA >= nowB:
    ans = "YES"
else:
    ans="NO"
print(ans)