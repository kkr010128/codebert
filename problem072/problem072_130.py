n = int(input())
c = 0
for _ in range(n):
    r = [int(e) for e in input().split(" ")]
    if(r[0] == r[1]):
        c += 1
    else:
        c = 0
    if(c == 3):
        print("Yes")
        break
else:
    print("No")

