a,b,c = map(int,input().split(" "))
right = c- a- b
if right > 0 and right ** 2 > 4 * a* b:
    print("Yes")
else:
    print("No")