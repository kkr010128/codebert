A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

distance = abs(A-B)
speed = V-W
if distance <= speed*T:
    print("YES")
else:
    print("NO")
