health1, strength1, health2, strength2 = map(int, input().split())
while health1 > 0 and health2 > 0:
    health2 -= strength1
    if health2 <= 0:
        print("Yes")
        break
    health1 -= strength2
    if health1 <= 0:
        print("No")
        break