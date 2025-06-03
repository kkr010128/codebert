def main():
    X = int(input())
    i = 1
    while True:
        if i * X % 360 == 0:
            print(i)
            break
        i += 1
main()  