H, A = map(int, input().split())
total = H // A
if H % A != 0:
    print(total+1)
else:
    print(total)