A, V = list(map(int, input().split()))
B, W = list(map(int, input().split()))
T = int(input())
 
if A == B:
    print("YES")
    exit()
 
if V == W:
    print("NO")
    exit()
 
time = abs(A - B) / (V - W)
if 0 <= time and time <= T:
    print("YES")
else:
    print("NO")
