def main():

    x,y = map(int, input().split())
    while y != 0:
        if x < y: x, y = y, x
        x, y = y, x % y
    print(x)

main()