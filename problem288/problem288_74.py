import math

N = int(input())

min_move_count = float("inf")
for i in range(1, int(math.sqrt(N)) + 1):
    if (N / i).is_integer():
        move_count = i + (N // i) - 2
        if move_count < min_move_count:
            min_move_count = move_count

print(min_move_count)