count = 0
for i in range(int(input())):
    l = list(map(int, input().split()))
    if l[0] == l[1]:
        count += 1
    elif l[0] != l[1]:
        count = 0
    if count >= 3:
        print("Yes")
        break
if count < 3:
    print("No")
