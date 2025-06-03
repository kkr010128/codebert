def main():

    Counter = 0
    Text_W = input()
    while True:
        Text_T = input()
        if "END_OF_TEXT" in Text_T:
            temp = Text_T.lower().split()
            for i in range(len(temp)):
                Counter += 1 if Text_W == temp[i] else 0
            break
        else:
            temp = Text_T.lower().split()
            for i in range(len(temp)):
                Counter += 1 if Text_W == temp[i] else 0

    print (Counter)

if __name__ == '__main__':
    main()
