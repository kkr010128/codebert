# -*- coding: utf-8 -*-

def main():

    X, Y, Z = map(int, input().split())

    X, Y = change(X, Y)
    X, Z = change(X, Z)

    print(X, Y ,Z)

def change(a, b):
    num = a
    a = b
    b = num

    return(a, b)

if __name__ == "__main__":
    main()