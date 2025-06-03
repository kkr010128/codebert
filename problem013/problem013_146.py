#-*- coding:utf-8 -*-

def main():
    n , data = input_data()
    vMax = float('-inf')
    vMin = data.pop(0)

    for Rj in data:
        if vMax < Rj - vMin:
            vMax = Rj - vMin
        if vMin > Rj:
            vMin = Rj

    print(vMax)

def input_data():
    n = int(input())
    lst = [int(input()) for i in range(n)]
    return (n , lst)

if __name__ == '__main__':
    main()