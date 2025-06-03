A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
firstDis = abs(A - B)
steps = (V - W)*T
print("YES" if firstDis <= steps else "NO")
