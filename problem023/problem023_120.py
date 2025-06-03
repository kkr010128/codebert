def main():
    n = int(input())
    operation = [input().split() for _ in range(n)]
    dictionary = {}
    
    for command, char in operation:
        if command == "insert":
            dictionary[char] = True
        elif command == "find":
            try:
                if dictionary[char]:
                    print("yes")
            except KeyError:
                print("no")
    return


if __name__ == "__main__":
    main()

