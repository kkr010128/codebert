length, time, speed = [int(x) for x in input().split(" ")]

if length / speed <= time:
    print("Yes")
else:
    print("No")