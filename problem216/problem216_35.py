A, B, C = map(int, input().split())
l = [A, B, C]
if len(set(l)) == 2:
    print("Yes")
else:
    print("No")
