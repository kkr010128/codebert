while True:
    n, goal = [int(x) for x in input().split(" ")]
    res =[]

    if n == goal == 0:
        break

    for first in range(1, n+1):
        for second in range(first+1, n+1):
            rem = goal - (first + second)
            if rem > second and n >= rem:
                res.append([first, second, rem])

    print(len(res))