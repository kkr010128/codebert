A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if A < B and B+W*T <= A+V*T:
    print("YES")
elif A > B and B-W*T >= A-V*T:
    print("YES")
else:
    print("NO")
