dice = [int(i) for i in input().split()]
n = int(input())
for _ in range(n):
    face = list(map(int, input().split()))
    if face in [[dice[0], dice[1]], [dice[1], dice[5]], [dice[5], dice[4]], [dice[4], dice[0]]]:
        print(dice[2])
    elif face in [[dice[0], dice[2]], [dice[2], dice[5]], [dice[5], dice[3]], [dice[3], dice[0]]]:
        print(dice[4])
    elif face in [[dice[0], dice[4]], [dice[4], dice[5]], [dice[5], dice[1]], [dice[1], dice[0]]]:
        print(dice[3])
    elif face in [[dice[0], dice[3]], [dice[3], dice[5]], [dice[5], dice[2]], [dice[2], dice[0]]]:
        print(dice[1])
    elif face in [[dice[1], dice[2]], [dice[2], dice[4]], [dice[4], dice[3]], [dice[3], dice[1]]]:
        print(dice[0])
    elif face in [[dice[1], dice[3]], [dice[3], dice[4]], [dice[4], dice[2]], [dice[2], dice[1]]]:
        print(dice[5])

