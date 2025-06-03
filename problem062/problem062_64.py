# coding: utf-8

while True:
    strnum = input().rstrip()
    if strnum == "0":
        break
    answer = sum(map(int, strnum))
    print(answer)