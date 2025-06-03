n = int(input())
room_list = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(n):
    b, f, r, v = map(int, input().split())
    room_list[b - 1][f - 1][r - 1] += v

output =[]
for i in range(4):
    for j in range(3):
        output = list(map(str, room_list[i][j]))
        print(" " + " ".join(output))
    if i < 3:
        print("#" * 20)