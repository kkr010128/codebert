A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
D = abs(A - B)
if (V > W) and \
   (D / (V - W) <= T):
    print("YES")
else:
    print("NO")