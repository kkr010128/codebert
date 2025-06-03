while 1:
    a = input()
    if a == "-":
        break
    b = int(input())
    for i in range(b):
        c = int(input())
        a = a[c:] + a[:c]
    print(a)
#word = "ABCDE"
#print(word[2:]) ## => CDE
#print(word[:3]) ## => ABC
