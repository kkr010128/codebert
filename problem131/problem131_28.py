A, V = map(int,input().split())
B, W = map(int,input().split())
T = int(input())
if (V <= W):
    print("NO")
elif(T < abs(A - B)/(V-W)):
    print("NO")
else:
    print("YES")
