# -*-coding:utf-8

def main():

    inputLine = int(input())

    taro = hanako = 0

    for i in range(inputLine):
        tokens = list(input().split())
        if(tokens[0] > tokens[1]):
            taro += 3
        elif(tokens[0] < tokens[1]):
            hanako += 3
        else:
            taro += 1
            hanako += 1

    print('%d %d' % (taro, hanako))



if __name__ == '__main__':
    main()