A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

a = abs(B-A)
if T * (V-W) >= a:
    print("YES")
else:print("NO")