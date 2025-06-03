def main():

    while True:
        strDeck = input()
        if strDeck == "-":
            break
        else:
            intTime = int(input())
            intNum = 0

            for _ in range(intTime):
                intNum += int(input())

            intLenDeck = len(strDeck)
            intShuffle = intNum % intLenDeck

            print(strDeck[intShuffle:]+strDeck[:intShuffle])


if __name__ == '__main__':
    main()

