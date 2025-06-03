def roll(die, d):
    if d == "E":
        return [die[3], die[1], die[0], die[5], die[4], die[2]]
    if d == "N":
        return [die[1], die[5], die[2], die[3], die[0], die[4]]
    if d == "S":
        return [die[4], die[0], die[2], die[3], die[5], die[1]]
    if d == "W":
        return [die[2], die[1], die[5], die[0], die[4], die[3]]
    if d == "L":
        return [die[0], die[3], die[1], die[4], die[2], die[5]]
    if d == "R":
        return [die[0], die[2], die[4], die[1], die[3], die[5]]

die = list(map(int, input().split()))
n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    if die[0] == a:
        pass
    elif die[1] == a:
        die = roll(die, "N")
    elif die[2] == a:
        die = roll(die, "W")
    elif die[3] == a:
        die = roll(die, "E")
    elif die[4] == a:
        die = roll(die, "S")
    elif die[5] == a:
        die = roll(roll(die, "E"), "E")
    while True:
        if die[1] == b:
            break
        die = roll(die, "R")
    print(die[2])