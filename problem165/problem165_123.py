# coding: utf-8

def main():
    n = int(input())
    goods = []
    for i in range(n):
        s = input()
        goods.append(s)
    print(len(set(goods)))
    
main()
