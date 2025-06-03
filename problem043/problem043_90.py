#coding:UTF-8

while True:
    n = map(int,raw_input().split())
    if (n[0] or n[1]) == 0:
        break
    n.sort()
    print n[0],n[1]