s = []
while True:
    hoge = input()
    if hoge == '-':
        break
    num = int(input())
    for i in range(num):
        h = int(input())
        hoge = hoge.replace(hoge,hoge[h:] + hoge[:h])
    s += [hoge]
for i in s: print(i)