h = int(input())
w = int(input())
n = int(input())

all_cell = 0
count = 0
while all_cell < n:
    if h > w:
        all_cell += h
        w -= 1
    else:
        all_cell += w
        h -= 1

    count += 1
print(count)