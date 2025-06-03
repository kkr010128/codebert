import sys
while True:
    height, width = map(int, raw_input().split())
    if height == 0 and width == 0:
        break
    for i in range(height):
        for j in range(width):
            if j % 2 == 0 and i % 2 == 0: #even n, even n
                sys.stdout.write("#")
            elif j % 2 != 0 and i % 2 == 0: #even n, odd n
                sys.stdout.write(".")
            elif j % 2 == 0 and i % 2 != 0: #odd n, even n
                sys.stdout.write(".")
            elif j % 2 != 0 and i % 2 != 0: #odd n, odd n
                sys.stdout.write("#")
        print
    print