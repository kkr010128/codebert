num = input()
for x in range(0, int(num)):
    l = map(int, input().split())
    lists = sorted(l)
    if lists[2] ** 2 == lists[0] ** 2 + lists[1] ** 2:
        print("YES")
    else:
        print("NO")