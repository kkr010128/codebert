d, t, s = map(int, input().split())
dist = t * s - d

if dist >= 0:
    print("Yes")
elif dist < 0:
    print("No")