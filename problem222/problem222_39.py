n = int(input())
alst = list(map(int, input().split()))
alst.sort()
bef = -1
for a in alst:
    if bef == a:
        print("NO")
        break
    bef = a
else:
    print("YES")