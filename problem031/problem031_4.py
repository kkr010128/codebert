# -*-coding:utf-8

import math

def main():

    while True:
        scoreNumber = int(input())
        if(scoreNumber == 0):
            break

        scoreList = list(map(float, input().split()))
        scoreAve = sum(scoreList) / len(scoreList)

        scoreSum = 0
        for i in scoreList:
            scoreSum += pow(i-scoreAve, 2) / len(scoreList)

        print(math.sqrt(scoreSum))


if __name__ == '__main__':
    main()