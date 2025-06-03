while True:
    string = input()
    if string == "0":break
    print(sum(int(x) for x in string))