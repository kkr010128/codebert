def main():

    TaroScore = HanaScore = 0
    n = int(input())
    for _ in range(n):
        [Taro, Hana] = list(input().lower().split())

        lenT = len(Taro)
        lenH = len(Hana)
        lenMin = min(lenT, lenH)

        if Taro == Hana:
            TaroScore += 1
            HanaScore += 1
        
        else:
            for i in range(lenMin+1):
                if Taro == '':
                    HanaScore += 3
                    break
                elif Hana == '':
                    TaroScore += 3
                    break
                elif ord(Taro[0]) > ord(Hana[0]):
                    TaroScore += 3
                    break
                elif ord(Taro[0]) < ord(Hana[0]):
                    HanaScore += 3
                    break
                else:
                    Taro = Taro[1:]
                    Hana = Hana[1:]

    print(TaroScore, HanaScore)

if __name__ == '__main__':
    main()

