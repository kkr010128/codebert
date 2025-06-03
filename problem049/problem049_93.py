matrix = []
while True:
    values = input()
    if '0 0' == values:
        break
    matrix.append([int(x) for x in values.split()])

for height, width in matrix:
    for i in range(height):
        print('#' * width)
    print()