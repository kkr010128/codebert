A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())
print("YES" if A+T*V>= B+T*W and A-T*V <= B-T*W else "NO")