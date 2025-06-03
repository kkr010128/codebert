while True:
    string = list(input())
    #1文字ずつ配列に入ってる
    if "-" in string:
        break

    shuffle = int(input())
    for i in range(shuffle):
        h = int(input())
        for j in range(h):
            string.append(string[0])
            del string[0]
    for i in range(len(string)):
        if i != len(string)-1:
            print(string[i],end="")
        else:
            print(string[i])

