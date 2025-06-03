def main():
    s = input()
    x = len(s)//2
    count = 0
    for i in range(x):
        if s[i] != s[(i+1)*-1]:
            count += 1
    print(count)


main()