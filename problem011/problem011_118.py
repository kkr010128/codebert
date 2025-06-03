# coding=utf-8

a, b = map(int, input().split())
if a > b:
    big_num = a
    sml_num = b
else:
    big_num = b
    sml_num = a

while True:
    diviser = big_num % sml_num
    if diviser == 0:
        break
    else:
        big_num = sml_num
        sml_num = diviser

print(sml_num)