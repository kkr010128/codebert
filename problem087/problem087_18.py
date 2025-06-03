def main():
    if sum(list(map(int, list(input())))) % 9:
        print("No")
    else:
        print("Yes")


main()
