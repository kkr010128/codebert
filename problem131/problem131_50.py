a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
yes = True
if v <= w:
    yes = False
elif abs(b - a) / (v - w) > t:
    yes = False
if yes:
    print("YES")
else:
    print("NO")