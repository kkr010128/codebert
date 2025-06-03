while True:
    height, width = [int(x) for x in input().split(" ")]
    if height == width == 0:
        break
    for i in range(height - 1):
        print("#" * width)
    print("#" * width + "\n")