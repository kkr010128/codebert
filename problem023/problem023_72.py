def main():
    n = int(input())
    d = set([])


    for i in range(n):
        command, string = input().split()
        if (command == 'insert'):
            d.add(string)
        elif (command == 'find'):
            if string in d:
                print('yes')
            else:
                print('no')

if __name__ == "__main__":
    main()