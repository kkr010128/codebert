A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if A > B:
    x = A
    A = B
    B = x
if V <= W:
    ans="NO"
elif T*V+A-B >= T*W:
    ans="YES"
else:
    ans="NO"
print(ans)